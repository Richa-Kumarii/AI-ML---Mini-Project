import React, { useState, useEffect } from 'react';
import { 
  History, 
  Trash2, 
  ExternalLink, 
  Clock, 
  Calendar, 
  Layers, 
  Search,
  Sparkles,
  AlertCircle
} from 'lucide-react';
import { getHistory, deleteHistoryItem } from '../services/api';

export default function HistoryVault({ onLoadGeneration }) {
  const [historyItems, setHistoryItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [deletingId, setDeletingId] = useState(null);
  const [error, setError] = useState('');

  const fetchHistory = async () => {
    try {
      setLoading(true);
      const data = await getHistory(50, 0);
      setHistoryItems(data);
      setError('');
    } catch (err) {
      console.error('Error fetching history:', err);
      setError('Could not load generation history from SQLite database.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  const handleDelete = async (e, id) => {
    e.stopPropagation();
    if (!window.confirm('Are you sure you want to delete this saved generation?')) return;
    try {
      setDeletingId(id);
      await deleteHistoryItem(id);
      setHistoryItems(prev => prev.filter(item => item.id !== id));
    } catch (err) {
      alert('Failed to delete item: ' + err.message);
    } finally {
      setDeletingId(null);
    }
  };

  const filteredItems = historyItems.filter(item => {
    const q = searchQuery.toLowerCase();
    return (
      item.topic.toLowerCase().includes(q) ||
      (item.tone && item.tone.toLowerCase().includes(q)) ||
      (item.language && item.language.toLowerCase().includes(q))
    );
  });

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="bg-[#0e1424] border border-slate-800 rounded-3xl p-6 sm:p-8 flex flex-col md:flex-row items-start md:items-center justify-between gap-6 shadow-2xl">
        <div>
          <h2 className="text-2xl sm:text-3xl font-black text-white flex items-center gap-3">
            <History className="w-6 h-6 text-purple-400" />
            <span>Entertainment Content Vault</span>
          </h2>
          <p className="text-xs sm:text-sm text-slate-400 mt-1">
            Persisted generations in SQLite. Revisit, re-export, and manage past entertainment assets.
          </p>
        </div>

        {/* Search Bar */}
        <div className="relative w-full md:w-72">
          <Search className="w-4 h-4 absolute left-3.5 top-3.5 text-slate-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search saved topics..."
            className="w-full pl-10 pr-4 py-2.5 rounded-xl bg-[#090d18] border border-slate-700/80 text-white placeholder-slate-500 text-xs focus:outline-none focus:border-purple-500"
          />
        </div>
      </div>

      {error && (
        <div className="p-4 rounded-xl bg-red-500/10 border border-red-500/30 text-red-300 text-sm flex items-center gap-3">
          <AlertCircle className="w-5 h-5 text-red-400 shrink-0" />
          <span>{error}</span>
        </div>
      )}

      {loading ? (
        <div className="text-center py-24 space-y-3">
          <div className="w-8 h-8 border-2 border-purple-500 border-t-transparent rounded-full animate-spin mx-auto" />
          <p className="text-sm text-slate-400">Accessing SQLite vault...</p>
        </div>
      ) : filteredItems.length === 0 ? (
        <div className="text-center py-20 p-8 rounded-3xl bg-[#0e1424] border border-slate-800 space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center mx-auto text-purple-400">
            <Sparkles className="w-6 h-6" />
          </div>
          <h3 className="text-lg font-bold text-white">No Saved Generations Found</h3>
          <p className="text-sm text-slate-400 max-w-sm mx-auto">
            {searchQuery
              ? `No results match "${searchQuery}". Try a different keyword.`
              : 'Generate content from the Studio to populate your persistent vault automatically.'}
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {filteredItems.map(item => {
            const platformCount = item.selected_platforms?.length || 0;
            const dateStr = item.created_at ? new Date(item.created_at).toLocaleDateString(undefined, {
              month: 'short',
              day: 'numeric',
              year: 'numeric',
              hour: '2-digit',
              minute: '2-digit'
            }) : 'Recent';

            return (
              <div
                key={item.id}
                onClick={() => onLoadGeneration(item)}
                className="group p-6 rounded-2xl bg-[#0e1424] border border-slate-800 hover:border-purple-500/50 transition-all duration-300 cursor-pointer shadow-lg hover:shadow-xl hover:-translate-y-0.5 flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between gap-4 mb-3">
                    <span className="text-[11px] font-semibold px-2.5 py-0.5 rounded-full bg-purple-500/10 text-purple-300 border border-purple-500/20">
                      {platformCount} Platforms
                    </span>
                    <div className="flex items-center gap-1.5 text-[11px] text-slate-400">
                      <Clock className="w-3.5 h-3.5" />
                      <span>{dateStr}</span>
                    </div>
                  </div>

                  <h3 className="text-base font-bold text-white group-hover:text-purple-300 transition-colors line-clamp-2 mb-2">
                    {item.topic}
                  </h3>

                  {item.description && (
                    <p className="text-xs text-slate-400 line-clamp-2 mb-4">
                      {item.description}
                    </p>
                  )}
                </div>

                <div className="pt-4 border-t border-slate-800/80 flex items-center justify-between">
                  <div className="flex flex-wrap gap-1.5">
                    <span className="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-mono">
                      {item.language}
                    </span>
                    <span className="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-mono">
                      {item.tone}
                    </span>
                  </div>

                  <div className="flex items-center gap-2">
                    <button
                      onClick={(e) => handleDelete(e, item.id)}
                      disabled={deletingId === item.id}
                      className="p-1.5 rounded-lg text-slate-500 hover:text-red-400 hover:bg-red-500/10 transition-colors"
                      title="Delete entry from SQLite"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                    <span className="text-xs font-semibold text-purple-400 group-hover:translate-x-0.5 transition-transform flex items-center gap-1">
                      <span>View</span>
                      <ExternalLink className="w-3.5 h-3.5" />
                    </span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

