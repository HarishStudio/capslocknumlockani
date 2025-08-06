#include <windows.h>
#include <stdbool.h>
#include <stdio.h>

bool capsLockState = false;
bool numLockState = false;

void checkAndTrigger() {
    SHORT capsState = GetKeyState(VK_CAPITAL);
    SHORT numState = GetKeyState(VK_NUMLOCK);

    bool newCaps = (capsState & 0x0001);
    bool newNum = (numState & 0x0001);

    if (newCaps != capsLockState) {
        capsLockState = newCaps;
        if (capsLockState) {
            ShellExecute(NULL, "open", "frontEnd.exe", "caps_on", NULL, SW_HIDE);
        } else {
            ShellExecute(NULL, "open", "frontEnd.exe", "caps_off", NULL, SW_HIDE);
        }
    }

    if (newNum != numLockState) {
        numLockState = newNum;
        if (numLockState) {
            ShellExecute(NULL, "open", "frontEnd.exe", "num_on", NULL, SW_HIDE);
        } else {
            ShellExecute(NULL, "open", "frontEnd.exe", "num_off", NULL, SW_HIDE);
        }
    }
}

int main() {
    // Initial state
    capsLockState = (GetKeyState(VK_CAPITAL) & 0x0001);
    numLockState = (GetKeyState(VK_NUMLOCK) & 0x0001);

    while (1) {
        checkAndTrigger();
        Sleep(100); // 100ms = 10 times/second
    }

    return 0;
}
