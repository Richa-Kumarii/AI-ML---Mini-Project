import React from 'react';
import { 
  Sparkles, 
  Layers, 
  History, 
  ExternalLink,
  Clapperboard,
  ShieldCheck,
  Zap,
  Activity
} from 'lucide-react';

export default function Navbar({ activeTab, setActiveTab, healthInfo }) {
  return (
    <header className="sticky top-0 z-50 backdrop-blur-xl bg-[#0b0f19]/80 border-b border-slate-800/80 px-4 lg:px-8 py-3.5 transition-all">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        
        {/* Brand Logo & Tag */}
        <div 
          onClick={() => setActiveTab('landing')}
          className="flex items-center gap-3 cursor-pointer group"
        >
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-purple-600 via-indigo-600 to-cyan-400 p-[1.5px] transition-transform duration-300 group-hover:scale-105">
            <div className="w-full h-full bg-[#0d1222] rounded-[10px] flex items-center justify-center">
              <Clapperboard className="w-5 h-5 text-purple-400 group-hover:text-cyan-300 transition-colors" />
            </div>
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-extrabold text-lg tracking-tight bg-gradient-to-r from-white via-slate-200 to-purple-200 bg-clip-text text-transparent">
                OmniContent<span className="text-purple-400 font-black">AI</span>
              </span>
              <span className="hidden sm:inline-block text-[10px] font-semibold tracking-wider uppercase px-2 py-0.5 rounded-full bg-purple-500/10 text-purple-300 border border-purple-500/20">
                NVIDIA Nemotron
              </span>
            </div>
            <p className="text-[11px] text-slate-400 hidden sm:block">
              Entertainment Multi-Platform AI Studio
            </p>
          </div>
        </div>

        {/* Navigation Tabs */}
        <nav className="flex items-center gap-1.5 sm:gap-2">
          <button
            onClick={() => setActiveTab('generator')}
            className={`flex items-center gap-2 px-3 sm:px-4 py-2 rounded-lg text-sm font-medium transition-all ${
              activeTab === 'generator'
                ? 'bg-purple-600 text-white shadow-lg shadow-purple-600/30'
                : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
            }`}
          >
            <Sparkles className="w-4 h-4 text-purple-300" />
            <span>Studio</span>
          </button>

          <button
            onClick={() => setActiveTab('history')}
            className={`flex items-center gap-2 px-3 sm:px-4 py-2 rounded-lg text-sm font-medium transition-all ${
              activeTab === 'history'
                ? 'bg-purple-600 text-white shadow-lg shadow-purple-600/30'
                : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
            }`}
          >
            <History className="w-4 h-4 text-purple-300" />
            <span>Vault</span>
          </button>

          <button
            onClick={() => setActiveTab('landing')}
            className={`hidden md:flex items-center gap-2 px-3.5 py-2 rounded-lg text-sm font-medium transition-all ${
              activeTab === 'landing'
                ? 'bg-slate-800 text-white'
                : 'text-slate-400 hover:text-white hover:bg-slate-800/40'
            }`}
          >
            <Layers className="w-4 h-4" />
            <span>Overview</span>
          </button>
        </nav>

        {/* NVIDIA Status Badge */}
        <div className="flex items-center gap-3">
          <div className="hidden lg:flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-900/90 border border-slate-800 text-xs text-slate-300">
            <span className={`w-2 h-2 rounded-full ${healthInfo?.nvidia_configured ? 'bg-emerald-400 animate-pulse' : 'bg-amber-400'}`} />
            <span className="font-mono text-[11px]">
              {healthInfo?.nvidia_configured ? 'NVIDIA NIM Active' : 'API Key Setup Needed'}
            </span>
          </div>

          <a
            href="https://build.nvidia.com/"
            target="_blank"
            rel="noopener noreferrer"
            className="hidden sm:flex items-center gap-1.5 text-xs text-slate-400 hover:text-purple-300 transition-colors"
          >
            <span>NVIDIA Cloud</span>
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
        </div>

      </div>
    </header>
  );
}

