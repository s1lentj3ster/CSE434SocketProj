#include <stdio.h>      /* for printf() and fprintf() */
#include <sys/socket.h> /* for socket() and bind() */
#include <arpa/inet.h>  /* for sockaddr_in and inet_ntoa() */
#include <stdlib.h>     /* for atoi() and exit() */
#include <string.h>     /* for memset() */
#include <unistd.h>     /* for close() */


//Client Register Info Structure
typedef struct{
    char name_client [20];
    char client_IP [20];
    int client_socket;

}Client_Info;

//Client list Structure
typedef struct{

    Client_Info new_Client;    

}Contact_List;


int main(int argc, char *argv[])
{


}

//Register Function
int register_Client(char client_contact, char client_IP, int client_Socket){

}

//Create Function
int create_List(char client_Contact_List){

}

//Query-List Function
void query_ClientList(){

}

//Join Function
int join_List(char contact_List, char contact_Name){

}

//Leave Function
void client_Leave(char contact_List, char contact_Name){

}

//Exit (Partial) Function
void client_Exit(char contact_Name){

}
