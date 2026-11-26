import React, { useState } from 'react';
import { 
  Copy, 
  Check, 
  RotateCw, 
  Edit3, 
  Download, 
  AlertTriangle, 
  CheckCircle2, 
  Video,
  Hash,
  FileText,
  Wand2,
  Save,
  X
} from 'lucide-react';
import { 
  InstagramIcon, 
  YoutubeIcon, 
  FacebookIcon, 
  XIcon, 
  LinkedInIcon 
} from './SocialIcons';

export default function PlatformCard({
  platformKey,
  data,
  topic,
  onRegenerate,
  onRewrite,
  isRegenerating
}) {
  const [copied, setCopied] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [editedContent, setEditedContent] = useState(data.main_content);
  const [showRewriteModal, setShowRewriteModal] = useState(false);
  const [customRewriteInstruction, setCustomRewriteInstruction] = useState('');
  const [quickRewriting, setQuickRewriting] = useState(false);

  const platformIcons = {
    instagram: { icon: InstagramIcon, color: 'text-pink-400', border: 'border-pink-500/30', badge: 'bg-pink-500/10 text-pink-300' },
    youtube: { icon: YoutubeIcon, color: 'text-red-400', border: 'border-red-500/30', badge: 'bg-red-500/10 text-red-300' },
    youtube_shorts: { icon: Video, color: 'text-orange-400', border: 'border-orange-500/30', badge: 'bg-orange-500/10 text-orange-300' },
    facebook: { icon: FacebookIcon, color: 'text-blue-400', border: 'border-blue-500/30', badge: 'bg-blue-500/10 text-blue-300' },
    x: { icon: XIcon, color: 'text-sky-300', border: 'border-sky-500/30', badge: 'bg-sky-500/10 text-sky-300' },
    linkedin: { icon: LinkedInIcon, color: 'text-cyan-400', border: 'border-cyan-500/30', badge: 'bg-cyan-500/10 text-cyan-300' },
  };

  const currentPlatform = platformIcons[platformKey] || {
    icon: FileText,
    color: 'text-purple-400',
    border: 'border-purple-500/30',
    badge: 'bg-purple-500/10 text-purple-300'
  };

  const Icon = currentPlatform.icon;

  const handleCopy = () => {
    let textToCopy = '';
    if (data.title) textToCopy += `TITLE: ${data.title}\n\n`;
    if (data.hook) textToCopy += `HOOK: ${data.hook}\n\n`;
    textToCopy += `${editedContent}\n\n`;
    if (data.call_to_action) textToCopy += `CTA: ${data.call_to_action}\n\n`;
    if (data.hashtags && data.hashtags.length > 0) {
      textToCopy += data.hashtags.map(t => t.startsWith('#') ? t : `#${t}`).join(' ');
    }

    navigator.clipboard.writeText(textToCopy);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleDownload = () => {
    let fullText = `=== OmniContent AI Generated Content ===\n`;
    fullText += `Platform: ${platformKey.toUpperCase()}\n`;
    fullText += `Topic: ${topic}\n`;
    fullText += `Date: ${new Date().toLocaleString()}\n`;
    fullText += `----------------------------------------\n\n`;
    if (data.title) fullText += `TITLE:\n${data.title}\n\n`;
    if (data.hook) fullText += `HOOK:\n${data.hook}\n\n`;
    fullText += `MAIN CONTENT:\n${editedContent}\n\n`;
    if (data.call_to_action) fullText += `CALL TO ACTION:\n${data.call_to_action}\n\n`;
    if (data.hashtags && data.hashtags.length > 0) {
      fullText += `HASHTAGS:\n${data.hashtags.map(t => t.startsWith('#') ? t : `#${t}`).join(' ')}\n\n`;
    }

    const blob = new Blob([fullText], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `${platformKey}_${topic.slice(0, 15).replace(/\s+/g, '_')}_content.txt`;
    link.click();
    URL.revokeObjectURL(url);
  };

  const handleSaveEdit = () => {
    data.main_content = editedContent;
    setIsEditing(false);
  };

  const handleQuickRewrite = async (instruction) => {
    setQuickRewriting(true);
    await onRewrite(platformKey, editedContent, instruction);
    setQuickRewriting(false);
    setShowRewriteModal(false);
  };

  return (
    <div className={`rounded-2xl bg-[#0f1527] border ${currentPlatform.border} flex flex-col justify-between overflow-hidden shadow-xl hover:shadow-2xl transition-all duration-300`}>
      {/* Top Card Header */}
      <div className="p-5 border-b border-slate-800/80 bg-slate-900/40">
        <div className="flex items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <div className={`p-2.5 rounded-xl bg-slate-800 border ${currentPlatform.border}`}>
              <Icon className={`w-5 h-5 ${currentPlatform.color}`} />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h3 className="font-bold text-white text-base capitalize">
                  {platformKey.replace('_', ' ')}
                </h3>
                <span className={`text-[11px] font-semibold px-2 py-0.5 rounded-full ${currentPlatform.badge}`}>
                  {data.content_type || 'Custom Post'}
                </span>
              </div>
              <div className="flex items-center gap-3 text-[11px] text-slate-400 mt-0.5">
                <span>{data.word_count || 0} words</span>
                <span>•</span>
                <span>{data.character_count || 0} characters</span>
              </div>
            </div>
          </div>

          {/* Validation Status Indicator */}
          <div className="flex items-center gap-1.5">
            {data.is_valid ? (
              <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 text-xs font-medium">
                <CheckCircle2 className="w-3.5 h-3.5" />
                <span>Validated</span>
              </div>
            ) : (
              <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20 text-xs font-medium" title={data.validation_warnings?.join(' | ')}>
                <AlertTriangle className="w-3.5 h-3.5" />
                <span>Caution</span>
              </div>
            )}
          </div>
        </div>

        {/* Validation warnings banner if present */}
        {data.validation_warnings && data.validation_warnings.length > 0 && (
          <div className="mt-3 p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/20 text-[11px] text-amber-300 space-y-1">
            {data.validation_warnings.map((w, idx) => (
              <div key={idx} className="flex items-start gap-1.5">
                <AlertTriangle className="w-3 h-3 text-amber-400 mt-0.5 shrink-0" />
                <span>{w}</span>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Card Body */}
      <div className="p-5 space-y-4 flex-1">
        {/* Title if applicable */}
        {data.title && (
          <div className="p-3 rounded-xl bg-[#090d18] border border-slate-800">
            <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
              Title / Hook Line
            </span>
            <p className="text-sm font-semibold text-white">
              {data.title}
            </p>
          </div>
        )}

        {/* Opening Hook if present */}
        {data.hook && (
          <div className="p-3 rounded-xl bg-purple-500/5 border border-purple-500/20">
            <span className="text-[10px] font-bold text-purple-300 uppercase tracking-wider block mb-1">
              Opening Retention Hook
            </span>
            <p className="text-xs text-purple-200 font-medium italic">
              "{data.hook}"
            </p>
          </div>
        )}

        {/* Main Content (Editable or Display) */}
        <div>
          <div className="flex items-center justify-between mb-1.5">
            <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">
              Content / Script Body
            </span>
            {isEditing ? (
              <button
                onClick={handleSaveEdit}
                className="flex items-center gap-1 text-xs text-emerald-400 hover:text-emerald-300 font-semibold"
              >
                <Save className="w-3.5 h-3.5" />
                <span>Save Edits</span>
              </button>
            ) : (
              <button
                onClick={() => setIsEditing(true)}
                className="flex items-center gap-1 text-xs text-slate-400 hover:text-purple-300 font-medium"
              >
                <Edit3 className="w-3.5 h-3.5" />
                <span>Quick Edit</span>
              </button>
            )}
          </div>

          {isEditing ? (
            <textarea
              rows={8}
              value={editedContent}
              onChange={(e) => setEditedContent(e.target.value)}
              className="w-full p-3.5 rounded-xl bg-[#090d18] border border-purple-500/50 text-white text-xs leading-relaxed focus:outline-none resize-y font-mono"
            />
          ) : (
            <div className="p-3.5 rounded-xl bg-[#090d18] border border-slate-800/80 text-xs sm:text-sm text-slate-200 leading-relaxed whitespace-pre-line max-h-80 overflow-y-auto">
              {editedContent}
            </div>
          )}
        </div>

        {/* Call to Action */}
        {data.call_to_action && (
          <div className="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300 flex items-center gap-2">
            <span className="font-bold text-purple-400 shrink-0">CTA:</span>
            <span>{data.call_to_action}</span>
          </div>
        )}

        {/* Hashtags */}
        {data.hashtags && data.hashtags.length > 0 && (
          <div className="flex flex-wrap gap-1.5 pt-1">
            {data.hashtags.map((tag, idx) => (
              <span
                key={idx}
                className="text-[11px] px-2 py-0.5 rounded-md bg-slate-800/70 text-purple-300 border border-slate-700/60 font-mono"
              >
                {tag.startsWith('#') ? tag : `#${tag}`}
              </span>
            ))}
          </div>
        )}
      </div>

      {/* Card Action Controls */}
      <div className="p-4 border-t border-slate-800/80 bg-slate-900/60 flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          {/* Copy Button */}
          <button
            onClick={handleCopy}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
              copied
                ? 'bg-emerald-600 text-white'
                : 'bg-slate-800 hover:bg-slate-700 text-slate-200'
            }`}
          >
            {copied ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
            <span>{copied ? 'Copied' : 'Copy'}</span>
          </button>

          {/* Download Button */}
          <button
            onClick={handleDownload}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-200 transition-all"
            title="Download formatted text file"
          >
            <Download className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Download</span>
          </button>
        </div>

        <div className="flex items-center gap-2">
          {/* AI Refine / Rewrite Button */}
          <button
            onClick={() => setShowRewriteModal(!showRewriteModal)}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-300 border border-indigo-500/30 transition-all"
          >
            <Wand2 className="w-3.5 h-3.5 text-indigo-400" />
            <span>AI Refine</span>
          </button>

          {/* Regenerate Button */}
          <button
            onClick={() => onRegenerate(platformKey)}
            disabled={isRegenerating}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-purple-600 hover:bg-purple-500 text-white shadow-md shadow-purple-600/20 transition-all disabled:opacity-50"
          >
            <RotateCw className={`w-3.5 h-3.5 ${isRegenerating ? 'animate-spin' : ''}`} />
            <span>Regenerate</span>
          </button>
        </div>
      </div>

      {/* AI Refine Modal / Accordion */}
      {showRewriteModal && (
        <div className="p-4 bg-[#090d18] border-t border-indigo-500/30 space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-indigo-300 flex items-center gap-1.5">
              <Wand2 className="w-3.5 h-3.5" />
              <span>Smart AI Modifier</span>
            </span>
            <button
              onClick={() => setShowRewriteModal(false)}
              className="text-slate-400 hover:text-white"
            >
              <X className="w-4 h-4" />
            </button>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
            {[
              'Make it funnier',
              'Make it more dramatic',
              'Make it shorter',
              'Convert to Hinglish'
            ].map(inst => (
              <button
                key={inst}
                onClick={() => handleQuickRewrite(inst)}
                disabled={quickRewriting}
                className="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-indigo-900/50 text-[11px] font-medium text-slate-300 border border-slate-700 hover:border-indigo-500/40 transition-colors text-left truncate"
              >
                {inst}
              </button>
            ))}
          </div>

          <div className="flex gap-2">
            <input
              type="text"
              value={customRewriteInstruction}
              onChange={(e) => setCustomRewriteInstruction(e.target.value)}
              placeholder="Custom direction e.g., 'Add a punchline about movie popcorn'..."
              className="flex-1 px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-white text-xs focus:outline-none focus:border-indigo-500"
            />
            <button
              onClick={() => customRewriteInstruction && handleQuickRewrite(customRewriteInstruction)}
              disabled={quickRewriting || !customRewriteInstruction.trim()}
              className="px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold disabled:opacity-50"
            >
              Apply
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
