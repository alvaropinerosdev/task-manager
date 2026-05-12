from task_manager import TaskManager;

def test_get_all():
    manager = TaskManager()
    all = manager.get_all()

    print(len(all))
    for task in all:
        print(task.__dict__)
    
test_get_all()

def test_get_by_id():
    manager = TaskManager()
    task = manager.get_by_id(1)

    if task is not None:
        print(task.__dict__)
    else:
        print("Task not found.")

test_get_by_id()

def test_add():
    manager = TaskManager()
    result = manager.add("Task de prueba", "Descripción de prueba", 1, 1, 1)

    if result is not None:
        print(f"Task added successfully. Affected rows: {result}")
    else:
        print("Failed to add task.")


test_add()

def test_delete():
    manager = TaskManager()
    result = manager.delete(7)

    if result:
        print("Task deleted successfully.")
    else:
        print("Failed to delete task or task not found.")

test_delete()

def test_update():
    manager = TaskManager()
    result = manager.update(6, nombre="Task actualizada", descripcion="Descripción actualizada")

    if isinstance(result, str):
        print(result)
    elif result is not None:
        print(f"Task updated successfully. Affected rows: {result}")
    else:
        print("Failed to update task.")

test_update()


