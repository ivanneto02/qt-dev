#ifndef BACKEND_H
#define BACKEND_H

#include <QObject>
#include <QString>

#include <qqml.h>

class Backend : public QObject {

    // Define Q_OBJECT
    Q_OBJECT
    Q_PROPERTY(QString userName READ userName WRITE setUserName NOTIFY userNameChanged)
    QML_ELEMENT

    private:
        // Data members
        QString m_userName;

    public:
        // Constructors
        explicit Backend(QObject *parent = nullptr);

        // Methods
        QString userName() const;
        void setUserName(const QString &name);
    
    signals:
        void userNameChanged();

};

#endif // BACKEND_H
