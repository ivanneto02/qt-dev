import QtQuick 2.0

Image {
    id: sample_button
    source: "images/sample_button.png"
    
    height: 35
    width: 100
    
    Text {
        anchors.centerIn: parent
        text: parent.width + "x" + parent.height
    }
}
