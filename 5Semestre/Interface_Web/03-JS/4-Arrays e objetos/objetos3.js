const task1 = {
    name: "Task1",
    createdAt: new Date(),
    updateAd: null,
    completed: false
}
const task2 = {
    createdAt: new Date(),
    updateAd: null,
    completed: false,
}

changeName: function(name) {
    this.name = new Date()
    this.updateAd = new Date()
}

task1.name = "task1 update"
task1.updateAd = new Date
task2.changeName("task2 update")
console.log(task1);
console.log(task2);
