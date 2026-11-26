import React from 'react';
import { 
  Sparkles, 
  ArrowRight, 
  Layers, 
  Film, 
  Share2, 
  Wand2, 
  CheckCircle2, 
  Video,
  Cpu,
  ShieldCheck,
  Zap,
  Globe2
} from 'lucide-react';
import { 
  InstagramIcon, 
  YoutubeIcon, 
  FacebookIcon, 
  XIcon, 
  LinkedInIcon 
} from './SocialIcons';

export default function LandingPage({ onGetStarted }) {
  const platforms = [
    { name: 'Instagram', icon: InstagramIcon, color: 'text-pink-400', border: 'border-pink-500/30', desc: 'Captions, Reel Hooks, Hashtags' },
    { name: 'YouTube', icon: YoutubeIcon, color: 'text-red-400', border: 'border-red-500/30', desc: 'High CTR Titles, Full Retention Scripts' },
    { name: 'YouTube Shorts', icon: Video, color: 'text-orange-400', border: 'border-orange-500/30', desc: '3-Sec Hooks, Dynamic Vertical Pacing' },
    { name: 'Facebook', icon: FacebookIcon, color: 'text-blue-400', border: 'border-blue-500/30', desc: 'Storytelling, Discussion Catalysts' },
    { name: 'X (Twitter)', icon: XIcon, color: 'text-sky-300', border: 'border-sky-500/30', desc: 'Single Posts (<280ch) & 1/N Threads' },
    { name: 'LinkedIn', icon: LinkedInIcon, color: 'text-cyan-400', border: 'border-cyan-500/30', desc: 'Industry Insights, Moral Takeaways' },
  ];

  const features = [
    {
      title: "Entertainment-Aware AI",
      description: "Powered by NVIDIA Nemotron 30B LLM to understand comedic timing, dramatic suspense, emotional resonance, and viral hook psychology.",
      icon: Film,
      gradient: "from-purple-500/20 to-pink-500/20"
    },
    {
      title: "6 Custom Platform Engines",
      description: "No generic copy-pasting. Each platform leverages specialized prompt architecture respecting algorithms, character caps, and audience behavior.",
      icon: Layers,
      gradient: "from-blue-500/20 to-cyan-500/20"
    },
    {
      title: "Tri-Lingual Fluency",
      description: "Seamlessly craft native content in pure English, authentic Devanagari Hindi, or modern conversational urban Hinglish.",
      icon: Globe2,
      gradient: "from-emerald-500/20 to-teal-500/20"
    },
    {
      title: "Built-In Platform Validator",
      description: "Real-time character verification, section completeness checking, keyword tracking, and automated 1-time AI constraint rewrites.",
      icon: ShieldCheck,
      gradient: "from-amber-500/20 to-orange-500/20"
    }
  ];

  return (
    <div className="space-y-24 py-8">
      {/* Hero Section */}
      <section className="relative text-center max-w-4xl mx-auto px-4 pt-12 pb-6">
        <div className="absolute inset-0 -top-20 bg-gradient-to-b from-purple-600/10 via-indigo-600/5 to-transparent blur-3xl pointer-events-none -z-10" />
        
        {/* Concept Pill */}
        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-purple-500/10 border border-purple-500/20 text-purple-300 text-xs sm:text-sm font-medium mb-6">
          <Zap className="w-4 h-4 text-purple-400 animate-bounce" />
          <span>ONE IDEA → 6 NATIVE ENTERTAINMENT ASSETS</span>
        </div>

        <h1 className="text-4xl sm:text-6xl font-black tracking-tight text-white leading-[1.15] mb-6">
          Transform One Idea into{' '}
          <span className="bg-gradient-to-r from-purple-400 via-pink-400 to-cyan-400 bg-clip-text text-transparent">
            Multi-Platform Entertainment Magic
          </span>
        </h1>

        <p className="text-base sm:text-xl text-slate-300 max-w-2xl mx-auto mb-10 leading-relaxed font-normal">
          Stop writing social media content from scratch for each network. Generate tailor-made scripts, hooks, threads, and captions crafted specifically for Instagram, YouTube, Shorts, Facebook, X, and LinkedIn.
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <button
            onClick={onGetStarted}
            className="w-full sm:w-auto flex items-center justify-center gap-2.5 px-8 py-4 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-semibold text-base shadow-xl shadow-purple-600/25 transition-all duration-200 transform hover:-translate-y-0.5"
          >
            <Sparkles className="w-5 h-5 text-purple-200" />
            <span>Launch Studio Dashboard</span>
            <ArrowRight className="w-4 h-4" />
          </button>

          <a
            href="https://build.nvidia.com/explore/discover"
            target="_blank"
            rel="noopener noreferrer"
            className="w-full sm:w-auto flex items-center justify-center gap-2 px-6 py-4 rounded-xl bg-slate-900 border border-slate-800 hover:border-slate-700 text-slate-300 hover:text-white text-base font-medium transition-all"
          >
            <Cpu className="w-4 h-4 text-emerald-400" />
            <span>NVIDIA NIM Powered</span>
          </a>
        </div>
      </section>

      {/* Platform Cards Grid */}
      <section className="max-w-7xl mx-auto px-4">
        <div className="text-center mb-10">
          <h2 className="text-2xl sm:text-3xl font-bold text-white mb-2">
            Tailored For Every Stage in Entertainment
          </h2>
          <p className="text-slate-400 text-sm sm:text-base">
            Every platform gets its own specialized prompt structure, tone tuning, and character limits.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6">
          {platforms.map((p, idx) => {
            const Icon = p.icon;
            return (
              <div
                key={idx}
                className="group relative p-6 rounded-2xl bg-slate-900/60 border border-slate-800/80 hover:border-purple-500/40 transition-all duration-300 hover:shadow-xl hover:shadow-purple-500/5 hover:-translate-y-1"
              >
                <div className="flex items-center gap-4 mb-4">
                  <div className={`p-3 rounded-xl bg-slate-800/90 border ${p.border}`}>
                    <Icon className={`w-6 h-6 ${p.color}`} />
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-white group-hover:text-purple-300 transition-colors">
                      {p.name}
                    </h3>
                    <span className="text-xs text-slate-400">Native Output Engine</span>
                  </div>
                </div>
                <p className="text-sm text-slate-300 leading-relaxed">
                  {p.desc}
                </p>
              </div>
            );
          })}
        </div>
      </section>

      {/* Core Features */}
      <section className="max-w-7xl mx-auto px-4">
        <div className="text-center mb-12">
          <h2 className="text-2xl sm:text-3xl font-bold text-white mb-3">
            Why Creators & Marketers Choose OmniContent
          </h2>
          <p className="text-slate-400 max-w-xl mx-auto text-sm sm:text-base">
            Engineered with deep prompt logic, safety fallbacks, and multi-language support.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {features.map((f, i) => {
            const Icon = f.icon;
            return (
              <div 
                key={i}
                className="p-8 rounded-2xl bg-[#0f1527] border border-slate-800 flex gap-5 items-start"
              >
                <div className={`p-3.5 rounded-xl bg-gradient-to-br ${f.gradient} border border-slate-700/50 shrink-0`}>
                  <Icon className="w-6 h-6 text-purple-300" />
                </div>
                <div>
                  <h3 className="text-lg font-bold text-white mb-2">{f.title}</h3>
                  <p className="text-sm text-slate-300 leading-relaxed">{f.description}</p>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* Live Content Comparison Example */}
      <section className="max-w-7xl mx-auto px-4">
        <div className="p-8 sm:p-12 rounded-3xl bg-gradient-to-br from-[#12192f] via-[#0d1326] to-[#090d1a] border border-slate-800/80">
          <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6 mb-8 border-b border-slate-800 pb-6">
            <div>
              <span className="text-xs font-bold text-purple-400 uppercase tracking-widest">
                Creative Demonstration
              </span>
              <h3 className="text-xl sm:text-2xl font-black text-white mt-1">
                Topic: "Behind the Scenes of a Sci-Fi Movie Climax"
              </h3>
            </div>
            <div className="flex items-center gap-2 text-xs font-medium text-slate-400 bg-slate-900/80 px-4 py-2 rounded-xl border border-slate-800">
              <CheckCircle2 className="w-4 h-4 text-emerald-400" />
              <span>Divergent Architectural Formats</span>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {/* Instagram reel sample */}
            <div className="p-5 rounded-xl bg-[#0b0f19] border border-pink-500/20 flex flex-col justify-between">
              <div>
                <div className="flex items-center gap-2 text-pink-400 font-semibold text-xs mb-3">
                  <InstagramIcon className="w-4 h-4" />
                  <span>Instagram Reel Hook & Caption</span>
                </div>
                <p className="text-sm text-slate-200 font-medium mb-3 italic">
                  "You think that gravity explosion was CGI? Watch what happened when the hydraulics snapped at 3 AM... 🎬🔥"
                </p>
                <p className="text-xs text-slate-400 leading-relaxed">
                  Scene breakdown with visual cues, high-energy emoji pacing, and 10 targeted tags (#SciFiCinema #PracticalEffects).
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-slate-800/60 text-[11px] text-pink-300/80">
                Format: 30s Visual Reel Script
              </div>
            </div>

            {/* YouTube Shorts sample */}
            <div className="p-5 rounded-xl bg-[#0b0f19] border border-orange-500/20 flex flex-col justify-between">
              <div>
                <div className="flex items-center gap-2 text-orange-400 font-semibold text-xs mb-3">
                  <Video className="w-4 h-4" />
                  <span>YouTube Shorts (9:16)</span>
                </div>
                <p className="text-sm text-slate-200 font-medium mb-3 italic">
                  "[Visual Hook: Camera crash zoom] 'Hollywood lied to you about zero gravity!' [00:02 - Fast cut to wire stunt]..."
                </p>
                <p className="text-xs text-slate-400 leading-relaxed">
                  Immediate 3-second retention lock, punchy sound effect callouts [Whoosh/Bass Drop], seamless loop ending.
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-slate-800/60 text-[11px] text-orange-300/80">
                Format: High-Retention Short Script
              </div>
            </div>

            {/* LinkedIn sample */}
            <div className="p-5 rounded-xl bg-[#0b0f19] border border-cyan-500/20 flex flex-col justify-between">
              <div>
                <div className="flex items-center gap-2 text-cyan-400 font-semibold text-xs mb-3">
                  <LinkedInIcon className="w-4 h-4" />
                  <span>LinkedIn Thought Leadership</span>
                </div>
                <p className="text-sm text-slate-200 font-medium mb-3 italic">
                  "What a $200M sci-fi set failure taught us about crisis management and agile creative leadership under pressure..."
                </p>
                <p className="text-xs text-slate-400 leading-relaxed">
                  Translates cinematic tension into 3 concrete leadership takeaways, professional spacing, and peer debate prompt.
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-slate-800/60 text-[11px] text-cyan-300/80">
                Format: Professional Industry Takeaway
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-800/80 py-8 text-center text-xs text-slate-500">
        <p>OmniContent AI Studio • Engineered with NVIDIA Nemotron LLM & FastAPI • Student Generative AI Capstone</p>
      </footer>
    </div>
  );
}
