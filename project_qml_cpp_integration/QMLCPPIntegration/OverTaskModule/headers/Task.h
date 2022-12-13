#ifndef TASK_H
#define TASK_H

#include <string>
#include "Taskcomponent.h"

using namespace std;

class Task : public TaskComponent {

    private:
        string title;
        string description;
        int priority;
        string classification;
        int durationHours;
        string dueDate;
        bool overdue;

    public:
        Task();
        
        void remove();
        void change_information();
};

#endif // TASK_H
