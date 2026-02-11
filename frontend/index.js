const API_BASE = 'http://localhost:5000/api';

document.addEventListener('DOMContentLoaded', () => {
  lucide.createIcons();
  setupTabs();
  setupEnhance();
  setupAnalyze();
  setupCompare();
  setupHistory();
});

// ============================================================================
// TAB NAVIGATION
// ============================================================================
function setupTabs() {
  const tabTriggers = document.querySelectorAll('.tab-trigger');
  const tabContents = document.querySelectorAll('.tab-content');
  
  tabTriggers.forEach(trigger => {
    trigger.addEventListener('click', () => {
      const tabName = trigger.getAttribute('data-tab');
      
      tabTriggers.forEach(t => t.classList.remove('active'));
      trigger.classList.add('active');
      
      tabContents.forEach(content => {
        content.classList.remove('active');
        if (content.id === `${tabName}-tab`) {
          content.classList.add('active');
        }
      });
      
      lucide.createIcons();
    });
  });
}

// ============================================================================
// ENHANCE TAB
// ============================================================================
function setupEnhance() {
  const originalPrompt = document.getElementById('original-prompt');
  const enhancedPrompt = document.getElementById('enhanced-prompt');
  const outputSection = document.getElementById('output-section');
  const enhanceBtn = document.getElementById('enhance-btn');
  const clearBtn = document.getElementById('clear-btn');
  const copyBtn = document.getElementById('copy-btn');
  const saveBtn = document.getElementById('save-btn');
  const intentBadge = document.getElementById('intent-badge');
  const intentText = document.getElementById('intent-text');
  
  let detectTimeout;
  originalPrompt.addEventListener('input', () => {
    clearTimeout(detectTimeout);
    detectTimeout = setTimeout(() => {
      if (originalPrompt.value.trim().length > 20) {
        detectIntent();
      }
    }, 1000);
  });
  
  async function detectIntent() {
    const prompt = originalPrompt.value.trim();
    if (!prompt) return;
    
    try {
      const response = await fetch(`${API_BASE}/detect-intent`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
      });
      
      const data = await response.json();
      if (data.success) {
        intentBadge.classList.remove('hidden');
        intentText.textContent = `${data.data.intent.toUpperCase()} • ${data.data.tone} • ${Math.round(data.data.confidence * 100)}% confident`;
      }
    } catch (error) {
      console.error('Intent detection failed:', error);
    }
  }
  
  enhanceBtn.addEventListener('click', async () => {
    const prompt = originalPrompt.value.trim();
    if (!prompt) {
      showToast('Empty Prompt', 'Please enter a prompt to enhance', 'error');
      return;
    }
    
    enhanceBtn.disabled = true;
    enhanceBtn.innerHTML = '<i data-lucide="loader"></i> Enhancing...';
    lucide.createIcons();
    
    try {
      const response = await fetch(`${API_BASE}/enhance`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
      });
      
      const data = await response.json();
      if (data.success) {
        enhancedPrompt.textContent = data.enhanced;
        outputSection.classList.remove('hidden');
        
        // Show which model was used
        const modelBadge = document.createElement('div');
        modelBadge.className = 'model-badge';
        modelBadge.textContent = `🤖 Powered by ${data.model.toUpperCase()}`;
        modelBadge.style.cssText = 'margin-top: 0.5rem; padding: 0.5rem 1rem; background: rgba(139, 92, 246, 0.1); border-radius: 0.5rem; font-size: 0.875rem; color: #a78bfa; display: inline-block;';
        
        // Remove old badge if exists
        const oldBadge = enhancedPrompt.parentElement.querySelector('.model-badge');
        if (oldBadge) oldBadge.remove();
        
        enhancedPrompt.parentElement.appendChild(modelBadge);
        
        showToast('Enhanced!', `Quality improved by ${data.improvement} points using ${data.model}`, 'success');
      }
    } catch (error) {
      showToast('Error', 'Failed to enhance prompt', 'error');
    } finally {
      enhanceBtn.disabled = false;
      enhanceBtn.innerHTML = '<i data-lucide="sparkles"></i> Enhance Prompt';
      lucide.createIcons();
    }
  });
  
  clearBtn.addEventListener('click', () => {
    originalPrompt.value = '';
    enhancedPrompt.textContent = '';
    outputSection.classList.add('hidden');
    intentBadge.classList.add('hidden');
  });
  
  copyBtn.addEventListener('click', () => {
    navigator.clipboard.writeText(enhancedPrompt.textContent);
    showToast('Copied!', 'Enhanced prompt copied to clipboard', 'success');
  });
  
  saveBtn.addEventListener('click', () => {
    const history = JSON.parse(localStorage.getItem('promptHistory') || '[]');
    history.unshift({
      id: Date.now().toString(),
      original: originalPrompt.value,
      enhanced: enhancedPrompt.textContent,
      timestamp: Date.now()
    });
    localStorage.setItem('promptHistory', JSON.stringify(history));
    showToast('Saved!', 'Prompt saved to history', 'success');
  });
}

// ============================================================================
// ANALYZE TAB
// ============================================================================
function setupAnalyze() {
  const heatmapPrompt = document.getElementById('heatmap-prompt');
  const analyzeBtn = document.getElementById('analyze-btn');
  const heatmapResults = document.getElementById('heatmap-results');
  
  analyzeBtn.addEventListener('click', async () => {
    const prompt = heatmapPrompt.value.trim();
    if (!prompt) {
      showToast('Empty Prompt', 'Please enter a prompt to analyze', 'error');
      return;
    }
    
    analyzeBtn.disabled = true;
    analyzeBtn.innerHTML = '<i data-lucide="loader"></i> Analyzing...';
    lucide.createIcons();
    
    try {
      const response = await fetch(`${API_BASE}/quality-heatmap`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
      });
      
      const data = await response.json();
      if (data.success) {
        displayHeatmap(data.data);
      }
    } catch (error) {
      showToast('Error', 'Failed to analyze prompt', 'error');
    } finally {
      analyzeBtn.disabled = false;
      analyzeBtn.innerHTML = '<i data-lucide="activity"></i> Analyze Quality';
      lucide.createIcons();
    }
  });
  
  function displayHeatmap(analysis) {
    heatmapResults.classList.remove('hidden');
    
    document.getElementById('overall-score').textContent = analysis.overall;
    document.getElementById('grade-badge').textContent = analysis.grade;
    
    const metrics = analysis.metrics;
    updateMetric('clarity', metrics.clarity.score);
    updateMetric('specificity', metrics.specificity.score);
    updateMetric('structure', metrics.structure.score);
    updateMetric('context', metrics.context.score);
    updateMetric('constraints', metrics.constraints.score);
    updateMetric('output-format', metrics.output_format.score);
    
    displaySuggestions(analysis.suggestions);
  }
  
  function updateMetric(name, score) {
    document.getElementById(`${name}-score`).textContent = `${score}/10`;
    document.getElementById(`${name}-bar`).style.width = `${(score / 10) * 100}%`;
  }
  
  function displaySuggestions(suggestions) {
    const container = document.getElementById('suggestions-list');
    container.innerHTML = '';
    
    if (suggestions.length === 0) {
      container.innerHTML = '<p style="color: #10b981;">✅ Your prompt looks great! No major issues found.</p>';
      return;
    }
    
    suggestions.forEach(sug => {
      const item = document.createElement('div');
      item.className = 'suggestion-item';
      item.innerHTML = `
        <div class="suggestion-category">❌ ${sug.category}</div>
        <div class="suggestion-issue">Issue: ${sug.issue}</div>
        <div class="suggestion-fix">✅ Fix: ${sug.fix}</div>
      `;
      container.appendChild(item);
    });
  }
}

// ============================================================================
// COMPARE TAB
// ============================================================================
function setupCompare() {
  const abtestPrompt = document.getElementById('abtest-prompt');
  const generateBtn = document.getElementById('generate-variations-btn');
  const variationsContainer = document.getElementById('variations-container');
  const recommendationBanner = document.getElementById('recommendation-banner');
  
  generateBtn.addEventListener('click', async () => {
    const prompt = abtestPrompt.value.trim();
    if (!prompt) {
      showToast('Empty Prompt', 'Please enter a prompt to test', 'error');
      return;
    }
    
    generateBtn.disabled = true;
    generateBtn.innerHTML = '<i data-lucide="loader"></i> Generating...';
    lucide.createIcons();
    
    try {
      const response = await fetch(`${API_BASE}/ab-test`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, include_comparison: true })
      });
      
      const data = await response.json();
      if (data.success) {
        displayVariations(data.data);
      }
    } catch (error) {
      showToast('Error', 'Failed to generate variations', 'error');
    } finally {
      generateBtn.disabled = false;
      generateBtn.innerHTML = '<i data-lucide="zap"></i> Generate Variations';
      lucide.createIcons();
    }
  });
  
  function displayVariations(comparison) {
    variationsContainer.classList.remove('hidden');
    
    ['concise', 'detailed', 'structured'].forEach(type => {
      const variation = comparison.variations[type];
      const card = document.getElementById(`variation-${type}`);
      
      card.querySelector('.variation-content').textContent = variation.text;
      card.querySelector('.quality-score').textContent = `${variation.quality.overall}/10`;
      card.querySelector('.length-stat').textContent = `${variation.length} chars`;
      
      // Show model used for each variation
      const modelInfo = variation.model ? ` (${variation.model})` : '';
      card.querySelector('.variation-badge').textContent = 
        card.querySelector('.variation-badge').textContent.split('(')[0].trim() + modelInfo;
    });
    
    recommendationBanner.classList.remove('hidden');
    document.getElementById('recommendation-text').textContent = 
      `🏆 Best: ${comparison.recommendation.best_variation.toUpperCase()} - ${comparison.recommendation.reason}`;
    
    document.querySelectorAll('.use-variation-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const type = btn.getAttribute('data-variation');
        const text = comparison.variations[type].text;
        document.getElementById('original-prompt').value = text;
        document.querySelector('.tab-trigger[data-tab="enhance"]').click();
        showToast('Loaded!', `${type} variation loaded`, 'success');
      });
    });
    
    lucide.createIcons();
  }
}

// ============================================================================
// HISTORY TAB
// ============================================================================
function setupHistory() {
  const historyList = document.getElementById('history-list');
  const historySearch = document.getElementById('history-search');
  const emptyHistory = document.getElementById('empty-history');
  
  function renderHistory() {
    const history = JSON.parse(localStorage.getItem('promptHistory') || '[]');
    const searchTerm = historySearch.value.toLowerCase();
    const filtered = history.filter(item => 
      item.original.toLowerCase().includes(searchTerm) || 
      item.enhanced.toLowerCase().includes(searchTerm)
    );
    
    if (filtered.length === 0) {
      emptyHistory.style.display = 'flex';
      historyList.innerHTML = '';
      historyList.appendChild(emptyHistory);
      return;
    }
    
    emptyHistory.style.display = 'none';
    historyList.innerHTML = '';
    
    filtered.forEach(item => {
      const div = document.createElement('div');
      div.className = 'history-item';
      div.innerHTML = `
        <div class="history-item-header">
          <div class="history-item-title">${item.original.substring(0, 80)}...</div>
          <button class="btn btn-ghost delete-btn" style="padding: 0.5rem;">
            <i data-lucide="trash-2"></i>
          </button>
        </div>
        <div class="history-item-date">${new Date(item.timestamp).toLocaleString()}</div>
      `;
      
      div.querySelector('.delete-btn').addEventListener('click', (e) => {
        e.stopPropagation();
        const history = JSON.parse(localStorage.getItem('promptHistory') || '[]');
        const updated = history.filter(h => h.id !== item.id);
        localStorage.setItem('promptHistory', JSON.stringify(updated));
        renderHistory();
        showToast('Deleted', 'Prompt removed from history', 'success');
      });
      
      div.addEventListener('click', () => {
        document.getElementById('original-prompt').value = item.original;
        document.getElementById('enhanced-prompt').textContent = item.enhanced;
        document.getElementById('output-section').classList.remove('hidden');
        document.querySelector('.tab-trigger[data-tab="enhance"]').click();
        showToast('Loaded', 'Prompt loaded from history', 'success');
      });
      
      historyList.appendChild(div);
    });
    
    lucide.createIcons();
  }
  
  historySearch.addEventListener('input', renderHistory);
  renderHistory();
}

// ============================================================================
// UTILITIES
// ============================================================================
function showToast(title, message, type = 'success') {
  const container = document.getElementById('toast-container');
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `
    <div class="toast-content">
      <div class="toast-title">${title}</div>
      <div class="toast-description">${message}</div>
    </div>
  `;
  
  container.appendChild(toast);
  
  setTimeout(() => {
    toast.style.animation = 'slideOut 0.3s ease forwards';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}
