import QtQuick 2.6
import QtQuick.Controls 2.0
import io.qt.examples.backend 1.0

Image {
    id: background_image
    source: "images/main_background.png"
    anchors.fill: parent
    
    TaskCanvas {
        visible: true
    }
}

// TextField object
/*
TextField {
    text: backend.userName
    placeholderText: qsTr("User name")
    anchors.centerIn: parent
    
    onEditingFinished: backend.userName = text
}
*/