import React, { useState } from 'react';
import { 
  Sparkles, 
  RotateCw, 
  Layers, 
  ArrowLeft, 
  Check, 
  DownloadCloud,
  FileCheck2,
  SlidersHorizontal,
  BookmarkPlus
} from 'lucide-react';
import PlatformCard from './PlatformCard';

export default function ResultsView({
  resultsData,
  onBackToEdit,
  onRegenerateSingle,
  onRewriteSingle,
  regeneratingPlatform
}) {
  const [filterPlatform, setFilterPlatform] = useState('all');
  const [copiedAll, setCopiedAll] = useState(false);

  const platforms = Object.keys(resultsData.results || {});
  const filteredPlatforms = filterPlatform === 'all'
    ? platforms
    : platforms.filter(p => p === filterPlatform);

  const handleCopyAll = () => {
    let combined = `==============================================\n`;
    combined += `OmniContent AI - Multi-Platform Output Pack\n`;
    combined += `Topic: ${resultsData.topic}\n`;
    combined += `==============================================\n\n`;

    platforms.forEach(p => {
      const item = resultsData.results[p];
      combined += `--- [${p.toUpperCase()}] ---\n`;
      if (item.title) combined += `Title: ${item.title}\n`;
      if (item.hook) combined += `Hook: ${item.hook}\n`;
      combined += `\n${item.main_content}\n\n`;
      if (item.call_to_action) combined += `Call To Action: ${item.call_to_action}\n`;
      if (item.hashtags?.length) combined += `Hashtags: ${item.hashtags.join(' ')}\n`;
      combined += `\n`;
    });

    navigator.clipboard.writeText(combined);
    setCopiedAll(true);
    setTimeout(() => setCopiedAll(false), 2000);
  };

  const handleDownloadAll = () => {
    let combined = `==============================================\n`;
    combined += `OmniContent AI - Multi-Platform Output Pack\n`;
    combined += `Topic: ${resultsData.topic}\n`;
    combined += `Generated: ${resultsData.created_at || new Date().toISOString()}\n`;
    combined += `==============================================\n\n`;

    platforms.forEach(p => {
      const item = resultsData.results[p];
      combined += `##############################################\n`;
      combined += `PLATFORM: ${p.toUpperCase()}\n`;
      combined += `FORMAT: ${item.content_type}\n`;
      combined += `STATS: ${item.word_count} words | ${item.character_count} chars\n`;
      combined += `##############################################\n\n`;
      if (item.title) combined += `TITLE:\n${item.title}\n\n`;
      if (item.hook) combined += `HOOK:\n${item.hook}\n\n`;
      combined += `MAIN SCRIPT / COPY:\n${item.main_content}\n\n`;
      if (item.call_to_action) combined += `CALL TO ACTION:\n${item.call_to_action}\n\n`;
      if (item.hashtags?.length) combined += `HASHTAGS:\n${item.hashtags.join(' ')}\n\n`;
      combined += `\n\n`;
    });

    const blob = new Blob([combined], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `omnicontent_${resultsData.topic.slice(0, 15).replace(/\s+/g, '_')}_all_platforms.txt`;
    link.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Header Bar */}
      <div className="bg-[#0e1424] border border-slate-800 rounded-3xl p-6 sm:p-8 flex flex-col md:flex-row items-start md:items-center justify-between gap-6 shadow-2xl">
        <div className="space-y-2">
          <button
            onClick={onBackToEdit}
            className="flex items-center gap-1.5 text-xs text-purple-400 hover:text-purple-300 font-semibold mb-2"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Modify Concept / Brief</span>
          </button>
          
          <h2 className="text-2xl sm:text-3xl font-black text-white">
            "{resultsData.topic}"
          </h2>
          <div className="flex flex-wrap items-center gap-3 text-xs text-slate-400">
            <span className="px-2.5 py-1 rounded-md bg-purple-500/10 text-purple-300 border border-purple-500/20 font-medium">
              {platforms.length} Platforms Generated
            </span>
            <span>•</span>
            <span className="flex items-center gap-1 text-emerald-400">
              <FileCheck2 className="w-3.5 h-3.5" />
              <span>NVIDIA Nemotron Verified</span>
            </span>
          </div>
        </div>

        {/* Action Controls */}
        <div className="flex flex-wrap items-center gap-3 w-full md:w-auto">
          <button
            onClick={handleCopyAll}
            className="flex-1 md:flex-none flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold transition-all shadow-md"
          >
            {copiedAll ? <Check className="w-4 h-4 text-emerald-400" /> : <Layers className="w-4 h-4" />}
            <span>{copiedAll ? 'All Content Copied!' : 'Copy All Platforms'}</span>
          </button>

          <button
            onClick={handleDownloadAll}
            className="flex-1 md:flex-none flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold transition-all shadow-lg shadow-purple-600/20"
          >
            <DownloadCloud className="w-4 h-4" />
            <span>Download All (.TXT)</span>
          </button>
        </div>
      </div>

      {/* Filter Tabs */}
      <div className="flex items-center gap-2 overflow-x-auto pb-2 border-b border-slate-800/80">
        <button
          onClick={() => setFilterPlatform('all')}
          className={`px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap transition-all ${
            filterPlatform === 'all'
              ? 'bg-purple-600 text-white shadow-md shadow-purple-600/30'
              : 'bg-slate-900/60 text-slate-400 hover:text-white border border-slate-800'
          }`}
        >
          All Platforms ({platforms.length})
        </button>

        {platforms.map(p => (
          <button
            key={p}
            onClick={() => setFilterPlatform(p)}
            className={`px-3.5 py-2 rounded-xl text-xs font-bold whitespace-nowrap capitalize transition-all ${
              filterPlatform === p
                ? 'bg-purple-600 text-white shadow-md shadow-purple-600/30'
                : 'bg-slate-900/60 text-slate-400 hover:text-white border border-slate-800'
            }`}
          >
            {p.replace('_', ' ')}
          </button>
        ))}
      </div>

      {/* Platform Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {filteredPlatforms.map(platformKey => (
          <PlatformCard
            key={platformKey}
            platformKey={platformKey}
            data={resultsData.results[platformKey]}
            topic={resultsData.topic}
            onRegenerate={onRegenerateSingle}
            onRewrite={onRewriteSingle}
            isRegenerating={regeneratingPlatform === platformKey}
          />
        ))}
      </div>
    </div>
  );
}

