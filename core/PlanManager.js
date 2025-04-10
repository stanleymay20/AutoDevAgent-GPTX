// core/PlanManager.js

class PlanManager {
    constructor() {
      this.tasks = [];
      this.currentTask = null;
    }
  
    load(tasksArray) {
      this.tasks = tasksArray;
      this.currentTask = this.tasks.length > 0 ? this.tasks[0] : null;
    }
  
    addTask(task) {
      this.tasks.push(task);
      if (!this.currentTask) this.currentTask = task;
    }
  
    completeCurrent() {
      if (this.currentTask) {
        const index = this.tasks.indexOf(this.currentTask);
        this.tasks.splice(index, 1);
        this.currentTask = this.tasks.length > 0 ? this.tasks[0] : null;
      }
    }
  
    getStatus() {
      return {
        total: this.tasks.length,
        current: this.currentTask
      };
    }
  }
  
  export default new PlanManager();
  