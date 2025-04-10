// core/memory/MemoryCore.js

export default class MemoryCore {
    constructor() {
      this.shortTerm = {};
      this.longTerm = this.loadMemory();
    }
  
    loadMemory() {
      const saved = localStorage.getItem('SEA_MEMORY');
      return saved ? JSON.parse(saved) : {};
    }
  
    saveMemory() {
      localStorage.setItem('SEA_MEMORY', JSON.stringify(this.longTerm));
    }
  
    remember(key, value, persistent = false) {
      if (persistent) {
        this.longTerm[key] = value;
        this.saveMemory();
      } else {
        this.shortTerm[key] = value;
      }
    }
  
    recall(key) {
      return this.shortTerm[key] || this.longTerm[key] || null;
    }
  
    forget(key) {
      delete this.shortTerm[key];
      delete this.longTerm[key];
      this.saveMemory();
    }
  
    dumpMemory() {
      return {
        shortTerm: this.shortTerm,
        longTerm: this.longTerm
      };
    }
  }
  