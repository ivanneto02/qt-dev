#include <iostream>
#include "backend.h"

// Constructors
Backend::Backend(QObject *parent) : QObject(parent) { }

// Setters
void Backend::setUserName(const QString &name) {
    if (name == m_userName) {
        return;
    }
    
    m_userName = name;
    std::cout << "Name: " << name.toStdString() << std::endl;
    emit userNameChanged();
}

// Getters
QString Backend::userName() const {
    return m_userName;
}