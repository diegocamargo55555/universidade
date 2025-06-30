function Task(name) {
    this.name = name
    this.createdAt = new Date()
    this.changeName = function (name) {
        this.name = name
    }
}

const task1 = new Task("Tarefa 1")
console.log(task1);
task1.changeName("Atualizada")
console.log(task1);

