import QtQuick 2.0

Image {
    height: 200
    width: 200
    
    id: task_box_image
    source: "images/box_background.png"
    
    Text {
        anchors.centerIn: parent
        text: parent.width + "x" + parent.height
    }
    
}

