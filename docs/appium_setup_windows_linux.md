# Настройка окружения Appium для Windows и Linux

## Windows

1. Установить Node.js LTS с официального сайта.
2. Проверить установку:

```powershell
node -v
npm -v
```

3. Установить Appium:

```powershell
npm install -g appium
appium driver install uiautomator2
```

4. Установить Python и зависимости проекта:

```powershell
pip install -r requirements.txt
```

5. Установить Android Studio.
6. Установить Android SDK.
7. Создать переменную среды `ANDROID_HOME`, например:

```text
C:\Users\User\AppData\Local\Android\Sdk
```

8. Добавить в `Path`:

```text
%ANDROID_HOME%\platform-tools
%ANDROID_HOME%\emulator
%ANDROID_HOME%\tools
%ANDROID_HOME%\tools\bin
```

9. Проверить ADB:

```powershell
adb version
adb devices
```

## Linux

1. Установить Node.js и npm:

```bash
sudo apt update
sudo apt install nodejs npm
```

2. Установить Appium:

```bash
sudo npm install -g appium
appium driver install uiautomator2
```

3. Установить Python-зависимости:

```bash
pip install -r requirements.txt
```

4. Установить Android Studio и Android SDK.
5. Добавить переменные окружения в `~/.bashrc` или `~/.zshrc`:

```bash
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/emulator
```

6. Проверить подключение устройства:

```bash
adb devices
```

## Подготовка Android-устройства

1. Включить режим разработчика.
2. Включить USB-отладку.
3. Подключить устройство к компьютеру.
4. Разрешить отладку на экране телефона.
5. Проверить командой:

```bash
adb devices
```
