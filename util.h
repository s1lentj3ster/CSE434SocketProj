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
