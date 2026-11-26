import React, { useState } from 'react';
import {
  Sparkles,
  Layers,
  Video,
  HelpCircle,
  Hash,
  Sliders,
  Check,
  AlertCircle
} from 'lucide-react';
import {
  InstagramIcon,
  YoutubeIcon,
  FacebookIcon,
  XIcon,
  LinkedInIcon
} from './SocialIcons';

export default function GeneratorForm({ onGenerate, isGenerating, initialData }) {
  const [topic, setTopic] = useState(initialData?.topic || '');
  const [description, setDescription] = useState(initialData?.description || '');
  const [selectedPlatforms, setSelectedPlatforms] = useState(
    initialData?.platforms || ['instagram', 'youtube', 'youtube_shorts', 'facebook', 'x', 'linkedin']
  );
  const [targetAudience, setTargetAudience] = useState(initialData?.target_audience || 'Entertainment & Pop Culture Fans');
  const [language, setLanguage] = useState(initialData?.language || 'English');
  const [tone, setTone] = useState(initialData?.tone || 'Motivational');
  const [contentType, setContentType] = useState(initialData?.content_type || 'Post');
  const [length, setLength] = useState(initialData?.length || 'Medium');
  const [keywordsInput, setKeywordsInput] = useState(
    initialData?.keywords ? initialData.keywords.join(', ') : ''
  );
  const [customInstructions, setCustomInstructions] = useState(initialData?.custom_instructions || '');
  const [validationError, setValidationError] = useState('');

  const platforms = [
    { id: 'instagram', name: 'Instagram', icon: InstagramIcon, color: 'hover:border-pink-500/50', activeBg: 'bg-pink-500/10 border-pink-500 text-pink-300' },
    { id: 'youtube', name: 'YouTube', icon: YoutubeIcon, color: 'hover:border-red-500/50', activeBg: 'bg-red-500/10 border-red-500 text-red-300' },
    { id: 'youtube_shorts', name: 'YouTube Shorts', icon: Video, color: 'hover:border-orange-500/50', activeBg: 'bg-orange-500/10 border-orange-500 text-orange-300' },
    { id: 'facebook', name: 'Facebook', icon: FacebookIcon, color: 'hover:border-blue-500/50', activeBg: 'bg-blue-500/10 border-blue-500 text-blue-300' },
    { id: 'x', name: 'X (Twitter)', icon: XIcon, color: 'hover:border-sky-500/50', activeBg: 'bg-sky-500/10 border-sky-500 text-sky-300' },
    { id: 'linkedin', name: 'LinkedIn', icon: LinkedInIcon, color: 'hover:border-cyan-500/50', activeBg: 'bg-cyan-500/10 border-cyan-500 text-cyan-300' },
  ];

  const tones = [
    'Funny',
    'Emotional',
    'Suspense',
    'Motivational',
    'Professional',
    'Casual',
    'Educational',
    'Storytelling',
    'Dramatic'
  ];

  const contentTypes = [
    'Post',
    'Caption',
    'Reel Script',
    'Video Script',
    'Short Script',
    'Story',
    'Dialogue',
    'Advertisement',
    'Thread',
    'Title and Description'
  ];

  const languages = [
    { id: 'English', label: 'English', desc: 'Global cinematic standard' },
    { id: 'Hindi', label: 'Hindi (हिंदी)', desc: 'Natural cultural resonance' },
    { id: 'Hinglish', label: 'Hinglish', desc: 'Modern urban Gen-Z blend' },
  ];

  const togglePlatform = (id) => {
    if (selectedPlatforms.includes(id)) {
      if (selectedPlatforms.length === 1) {
        setValidationError('At least one platform must be selected.');
        return;
      }
      setSelectedPlatforms(selectedPlatforms.filter(p => p !== id));
    } else {
      setSelectedPlatforms([...selectedPlatforms, id]);
    }
    setValidationError('');
  };

  const selectAllPlatforms = () => {
    setSelectedPlatforms(platforms.map(p => p.id));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!topic.trim()) {
      setValidationError('Please enter a central creative topic or concept.');
      return;
    }
    if (selectedPlatforms.length === 0) {
      setValidationError('Please select at least one target social platform.');
      return;
    }

    setValidationError('');

    const keywords = keywordsInput
      .split(',')
      .map(k => k.trim())
      .filter(k => k.length > 0);

    onGenerate({
      topic: topic.trim(),
      description: description.trim() || null,
      platforms: selectedPlatforms,
      target_audience: targetAudience.trim() || 'General Audience',
      language,
      tone,
      content_type: contentType,
      length,
      keywords,
      custom_instructions: customInstructions.trim() || null,
    });
  };

  return (
    <div className="bg-[#0e1424] border border-slate-800 rounded-3xl p-6 sm:p-8 shadow-2xl relative overflow-hidden">
      <div className="flex items-center justify-between pb-6 border-b border-slate-800 mb-6">
        <div>
          <h2 className="text-xl sm:text-2xl font-black text-white flex items-center gap-2.5">
            <Sliders className="w-5 h-5 text-purple-400" />
            <span>Creative Brief Engine</span>
          </h2>
          <p className="text-xs sm:text-sm text-slate-400 mt-1">
            Configure your core entertainment topic and let NVIDIA Nemotron adapt it natively.
          </p>
        </div>

        <button
          type="button"
          onClick={selectAllPlatforms}
          className="text-xs text-purple-400 hover:text-purple-300 font-medium px-3 py-1.5 rounded-lg bg-purple-500/10 border border-purple-500/20 transition-colors"
        >
          Select All 6 Platforms
        </button>
      </div>

      {validationError && (
        <div className="mb-6 p-4 rounded-xl bg-red-500/10 border border-red-500/30 flex items-center gap-3 text-red-300 text-sm">
          <AlertCircle className="w-5 h-5 shrink-0 text-red-400" />
          <span>{validationError}</span>
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Core Topic Field */}
        <div>
          <label className="block text-sm font-semibold text-slate-200 mb-2">
            Central Entertainment Topic or Idea <span className="text-purple-400">*</span>
          </label>
          <input
            type="text"
            required
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            placeholder="e.g., A time-travel thriller where each jump causes an alternate soundtrack to play"
            className="w-full px-4 py-3.5 rounded-xl bg-[#090d18] border border-slate-700/80 text-white placeholder-slate-500 text-sm focus:outline-none focus:border-purple-500 focus:ring-1 focus:ring-purple-500 transition-all"
          />
        </div>

        {/* Optional Context/Description */}
        <div>
          <label className="block text-sm font-semibold text-slate-200 mb-2">
            Detailed Narrative / Story Context <span className="text-xs font-normal text-slate-400">(Optional)</span>
          </label>
          <textarea
            rows={3}
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Provide backstory, character dynamics, punchlines, or key plot points you want preserved..."
            className="w-full px-4 py-3 rounded-xl bg-[#090d18] border border-slate-700/80 text-white placeholder-slate-500 text-sm focus:outline-none focus:border-purple-500 focus:ring-1 focus:ring-purple-500 transition-all resize-none"
          />
        </div>

        {/* Platform Multi-Selector */}
        <div>
          <label className="block text-sm font-semibold text-slate-200 mb-2.5">
            Target Social Platforms <span className="text-purple-400">*</span>
            <span className="text-xs font-normal text-slate-400 ml-2">
              ({selectedPlatforms.length} of {platforms.length} selected)
            </span>
          </label>

          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
            {platforms.map((p) => {
              const Icon = p.icon;
              const isSelected = selectedPlatforms.includes(p.id);
              return (
                <button
                  type="button"
                  key={p.id}
                  onClick={() => togglePlatform(p.id)}
                  className={`flex flex-col items-center justify-center p-3.5 rounded-xl border transition-all text-center ${isSelected
                    ? p.activeBg
                    : 'bg-[#090d18] border-slate-800 text-slate-400 hover:text-slate-200 ' + p.color
                    }`}
                >
                  <Icon className="w-5 h-5 mb-1.5" />
                  <span className="text-xs font-semibold">{p.name}</span>
                  {isSelected && (
                    <div className="mt-1 flex items-center gap-1 text-[10px] font-bold">
                      <Check className="w-3 h-3" />
                      <span>Active</span>
                    </div>
                  )}
                </button>
              );
            })}
          </div>
        </div>

        {/* Language, Tone & Target Audience Row */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
          {/* Language Selection */}
          <div>
            <label className="block text-sm font-semibold text-slate-200 mb-2">
              Language
            </label>
            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
              className="w-full px-3.5 py-3 rounded-xl bg-[#090d18] border border-slate-700/80 text-white text-sm focus:outline-none focus:border-purple-500"
            >
              {languages.map(lang => (
                <option key={lang.id} value={lang.id} className="bg-slate-900">
                  {lang.label} - {lang.desc}
                </option>
              ))}
            </select>
          </div>

          {/* Tone Selection */}
          <div>
            <label className="block text-sm font-semibold text-slate-200 mb-2">
              Tone & Mood
            </label>
            <select
              value={tone}
              onChange={(e) => setTone(e.target.value)}
              className="w-full px-3.5 py-3 rounded-xl bg-[#090d18] border border-slate-700/80 text-white text-sm focus:outline-none focus:border-purple-500"
            >
              {tones.map(t => (
                <option key={t} value={t} className="bg-slate-900">
                  {t}
                </option>
              ))}
            </select>
          </div>

          {/* Length */}
          <div>
            <label className="block text-sm font-semibold text-slate-200 mb-2">
              Content Length
            </label>
            <div className="grid grid-cols-3 gap-2">
              {['Short', 'Medium', 'Long'].map(len => (
                <button
                  type="button"
                  key={len}
                  onClick={() => setLength(len)}
                  className={`py-2.5 rounded-xl text-xs font-semibold border transition-all ${length === len
                    ? 'bg-purple-600 text-white border-purple-500 shadow-md shadow-purple-600/30'
                    : 'bg-[#090d18] text-slate-400 border-slate-800 hover:border-slate-700'
                    }`}
                >
                  {len}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Content Type, Target Audience & Keywords Row */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
          {/* Format / Content Type */}
          <div>
            <label className="block text-sm font-semibold text-slate-200 mb-2">
              Primary Format
            </label>
            <select
              value={contentType}
              onChange={(e) => setContentType(e.target.value)}
              className="w-full px-3.5 py-3 rounded-xl bg-[#090d18] border border-slate-700/80 text-white text-sm focus:outline-none focus:border-purple-500"
            >
              {contentTypes.map(ct => (
                <option key={ct} value={ct} className="bg-slate-900">
                  {ct}
                </option>
              ))}
            </select>
          </div>

          {/* Target Audience */}
          <div>
            <label className="block text-sm font-semibold text-slate-200 mb-2">
              Target Audience
            </label>
            <input
              type="text"
              value={targetAudience}
              onChange={(e) => setTargetAudience(e.target.value)}
              placeholder="e.g., Marvel fans, Indie filmmakers, Film students"
              className="w-full px-3.5 py-3 rounded-xl bg-[#090d18] border border-slate-700/80 text-white placeholder-slate-500 text-sm focus:outline-none focus:border-purple-500"
            />
          </div>

          {/* Mandatory Keywords */}
          <div>
            <label className="block text-sm font-semibold text-slate-200 mb-2">
              Mandatory Keywords <span className="text-xs font-normal text-slate-400">(Comma separated)</span>
            </label>
            <input
              type="text"
              value={keywordsInput}
              onChange={(e) => setKeywordsInput(e.target.value)}
              placeholder="e.g., plot twist, cliffhanger, VFX"
              className="w-full px-3.5 py-3 rounded-xl bg-[#090d18] border border-slate-700/80 text-white placeholder-slate-500 text-sm focus:outline-none focus:border-purple-500"
            />
          </div>
        </div>

        {/* Optional Custom Instructions */}
        <div>
          <label className="block text-sm font-semibold text-slate-200 mb-2">
            Special Creative Directives <span className="text-xs font-normal text-slate-400">(Optional)</span>
          </label>
          <input
            type="text"
            value={customInstructions}
            onChange={(e) => setCustomInstructions(e.target.value)}
            placeholder="e.g., End with a cliffhanger question asking viewers to choose between two characters"
            className="w-full px-4 py-3 rounded-xl bg-[#090d18] border border-slate-700/80 text-white placeholder-slate-500 text-sm focus:outline-none focus:border-purple-500"
          />
        </div>

        {/* Submit Button */}
        <div className="pt-2">
          <button
            type="submit"
            disabled={isGenerating}
            className={`w-full py-4 rounded-xl font-bold text-base flex items-center justify-center gap-3 transition-all ${isGenerating
              ? 'bg-purple-800/50 text-purple-200 cursor-not-allowed'
              : 'bg-gradient-to-r from-purple-600 via-indigo-600 to-cyan-500 hover:from-purple-500 hover:to-cyan-400 text-white shadow-xl shadow-purple-600/30 transform hover:-translate-y-0.5'
              }`}
          >
            {isGenerating ? (
              <>
                <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                <span>Generating Platform Content with NVIDIA Nemotron...</span>
              </>
            ) : (
              <>
                <Sparkles className="w-5 h-5 text-purple-200" />
                <span>Generate Content for {selectedPlatforms.length} Platforms</span>
              </>
            )}
          </button>
        </div>
      </form>
    </div>
  );
}
