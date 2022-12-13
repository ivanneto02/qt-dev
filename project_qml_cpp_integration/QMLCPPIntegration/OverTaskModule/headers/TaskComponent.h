#ifndef TASKCOMPONENT_H
#define TASKCOMPONENT_H

class TaskComponent {

    public:
        // Constructors
        TaskComponent();
        
        // Modifiers
        void remove();
        void changeInformation();
        void removeAll();
        void addTask(TaskComponent*);
        void removeTask(TaskComponent*);
        void upgradeTask(TaskComponent*);
};

#endif // TASKCOMPONENT_H
