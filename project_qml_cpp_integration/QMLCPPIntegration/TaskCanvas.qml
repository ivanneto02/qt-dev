import QtQuick 2.0
import QtQuick.Layouts
import QtQuick.Controls

Item {
    id: canvas_root
    
    x: 0
    y: 0
   
    Rectangle {
        id: selection_rectangle
        x: parent.x + 10
        y: parent.y + 10
        
        width: background_image.width - 20
        height: 35
        color: "black"
        
        SampleButton {}
        
    }
    Rectangle {
        id: canvas_rectangle
        
        x: parent.x + 10
        y: parent.y + 65
        width: background_image.width - 20
        height: background_image.height - 75
        color: "black"
    
        Grid {
            id: task_grid
            
            columns: 4
            
            // Task Box items
            TaskBox {}
            TaskBox {}
            TaskBox {}
            TaskBox {}
            TaskBox {}
            TaskBox {}
            TaskBox {}
            TaskBox {}
            
        }
    
    }
    
}
