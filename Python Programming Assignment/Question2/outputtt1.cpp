
#include <stdio.h>
#include <stdlib.h>
#include <termios.h>
#include <termios.h>
#include <unistd.h>
static struct termios initial_settings, new_settings;
static int peek_character = -1;
haracter != -1;
return 1;
new_settings.c_cc[VMIN]=0;
tcsetattr(0, TCSANOW, &new_settings);
nread = read(0,&ch,1);
new_settings.c_cc[VMIN]=1;
tcsetattr(0, TCSANOW, &new_settings);
if(nread == 1) {
peek_character = ch;
return 1;
}
return 0;
}

int readch()
{
char ch;
if(peek_character != -1) {
ch = peek_character;
peek_character = -1;
return ch;
}
read(0,&ch,1);
return ch;
}
int main()
{
int ch = 0;
init_keyboard();
while(ch != 'q') {
printf("looping\n");
if(ch==65)
{
printf("\33[%dA",3);
fflush(stdout);
}
if(ch==66)
{
printf("\33[%dB",3);
fflush(stdout);
}
if(ch==67)
{
printf("\33[%dC",3);
fflush(stdout);
}
if(ch==68)
{
printf("\33[%dD",3);
fflush(stdout);
}
sleep(1);
if(kbhit()) {
ch = readch();
printf("you hit %c\n",ch);
}
}
close_keyboard();
exit(0);
}
