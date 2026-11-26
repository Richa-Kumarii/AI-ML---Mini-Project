import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import LandingPage from './components/LandingPage';
import GeneratorForm from './components/GeneratorForm';
import ResultsView from './components/ResultsView';
import HistoryVault from './components/HistoryVault';
import { 
  checkHealth, 
  generateContent, 
  regeneratePlatformContent, 
  rewriteContent 
} from './services/api';
import { AlertCircle, CheckCircle2 } from 'lucide-react';

export default function App() {
  const [activeTab, setActiveTab] = useState('landing'); // 'landing' | 'generator' | 'results' | 'history'
  const [healthInfo, setHealthInfo] = useState(null);
  const [isGenerating, setIsGenerating] = useState(false);
  const [regeneratingPlatform, setRegeneratingPlatform] = useState(null);
  const [currentResults, setCurrentResults] = useState(null);
  const [lastFormConfig, setLastFormConfig] = useState(null);
  const [appNotification, setAppNotification] = useState(null);

  // Poll / check backend health on mount
  useEffect(() => {
    const testHealth = async () => {
      try {
        const h = await checkHealth();
        setHealthInfo(h);
      } catch (err) {
        console.warn('Backend not responding to health check:', err);
        setHealthInfo({ status: 'offline', nvidia_configured: false });
      }
    };
    testHealth();
  }, []);

  const showNotification = (message, type = 'info') => {
    setAppNotification({ message, type });
    setTimeout(() => {
      setAppNotification(null);
    }, 4500);
  };

  const handleGenerate = async (formData) => {
    setIsGenerating(true);
    setLastFormConfig(formData);
    try {
      const response = await generateContent(formData);
      setCurrentResults(response);
      setActiveTab('results');
      showNotification('Content generated & validated successfully!', 'success');
    } catch (err) {
      console.error('Generation error:', err);
      const detail = err.response?.data?.detail || err.message;
      showNotification(`Generation error: ${detail}`, 'error');
    } finally {
      setIsGenerating(false);
    }
  };

  const handleRegenerateSingle = async (platform) => {
    if (!lastFormConfig && !currentResults) return;
    setRegeneratingPlatform(platform);
    try {
      const payload = {
        generation_id: currentResults?.id || null,
        platform: platform,
        topic: lastFormConfig?.topic || currentResults?.topic,
        description: lastFormConfig?.description,
        target_audience: lastFormConfig?.target_audience,
        language: lastFormConfig?.language || 'English',
        tone: lastFormConfig?.tone || 'Motivational',
        content_type: lastFormConfig?.content_type || 'Post',
        length: lastFormConfig?.length || 'Medium',
        keywords: lastFormConfig?.keywords || [],
        custom_instructions: lastFormConfig?.custom_instructions,
      };

      const newPlatformResult = await regeneratePlatformContent(payload);
      setCurrentResults(prev => ({
        ...prev,
        results: {
          ...prev.results,
          [platform]: newPlatformResult
        }
      }));
      showNotification(`Regenerated ${platform.replace('_', ' ')} content!`, 'success');
    } catch (err) {
      console.error('Single regenerate error:', err);
      showNotification(`Failed to regenerate: ${err.message}`, 'error');
    } finally {
      setRegeneratingPlatform(null);
    }
  };

  const handleRewriteSingle = async (platform, currentContent, instruction) => {
    try {
      const payload = {
        platform,
        topic: currentResults?.topic || lastFormConfig?.topic,
        current_content: currentContent,
        instruction,
        language: lastFormConfig?.language,
        tone: lastFormConfig?.tone,
        length: lastFormConfig?.length,
      };
      const refinedResult = await rewriteContent(payload);
      setCurrentResults(prev => ({
        ...prev,
        results: {
          ...prev.results,
          [platform]: refinedResult
        }
      }));
      showNotification(`Refined ${platform.replace('_', ' ')} based on instruction!`, 'success');
    } catch (err) {
      console.error('Rewrite error:', err);
      showNotification(`Rewrite failed: ${err.message}`, 'error');
    }
  };

  const handleLoadFromHistory = (item) => {
    setCurrentResults({
      id: item.id,
      topic: item.topic,
      results: item.results,
      created_at: item.created_at
    });
    setLastFormConfig({
      topic: item.topic,
      description: item.description,
      platforms: item.selected_platforms,
      target_audience: item.target_audience,
      language: item.language,
      tone: item.tone,
      content_type: item.content_type,
      length: item.length,
      keywords: item.keywords,
      custom_instructions: item.custom_instructions
    });
    setActiveTab('results');
    showNotification(`Loaded "${item.topic.slice(0, 25)}..." from Vault!`, 'info');
  };

  return (
    <div className="min-h-screen bg-[#0b0f19] text-slate-100 flex flex-col selection:bg-purple-500 selection:text-white">
      {/* Top Navigation */}
      <Navbar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        healthInfo={healthInfo}
      />

      {/* App Notification Toast */}
      {appNotification && (
        <div className="fixed bottom-6 right-6 z-50 animate-bounce">
          <div className={`p-4 rounded-2xl shadow-2xl flex items-center gap-3 text-xs sm:text-sm font-semibold border ${
            appNotification.type === 'error'
              ? 'bg-red-950/90 text-red-200 border-red-500/50'
              : appNotification.type === 'success'
              ? 'bg-emerald-950/90 text-emerald-200 border-emerald-500/50'
              : 'bg-purple-950/90 text-purple-200 border-purple-500/50'
          }`}>
            {appNotification.type === 'error' ? (
              <AlertCircle className="w-5 h-5 text-red-400" />
            ) : (
              <CheckCircle2 className="w-5 h-5 text-emerald-400" />
            )}
            <span>{appNotification.message}</span>
          </div>
        </div>
      )}

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-8">
        {activeTab === 'landing' && (
          <LandingPage onGetStarted={() => setActiveTab('generator')} />
        )}

        {activeTab === 'generator' && (
          <div className="max-w-4xl mx-auto">
            <GeneratorForm
              onGenerate={handleGenerate}
              isGenerating={isGenerating}
              initialData={lastFormConfig}
            />
          </div>
        )}

        {activeTab === 'results' && currentResults && (
          <ResultsView
            resultsData={currentResults}
            onBackToEdit={() => setActiveTab('generator')}
            onRegenerateSingle={handleRegenerateSingle}
            onRewriteSingle={handleRewriteSingle}
            regeneratingPlatform={regeneratingPlatform}
          />
        )}

        {activeTab === 'history' && (
          <HistoryVault onLoadGeneration={handleLoadFromHistory} />
        )}
      </main>
    </div>
  );
}
