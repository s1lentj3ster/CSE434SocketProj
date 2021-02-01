#include "defns.h"

#include <stdio.h>      /* for printf() and fprintf() */
#include <sys/socket.h> /* for socket(), connect(), sendto(), and recvfrom() */
#include <arpa/inet.h>  /* for sockaddr_in and inet_addr() */
#include <stdlib.h>     /* for atoi() and exit() */
#include <string.h>     /* for memset() */
#include <unistd.h>     /* for close() */

#define ITERATIONS	5

void DieWithError(const char *errorMessage) /* External error handling function */
{
    perror(errorMessage);
    exit(1);
}

int main(int argc, char *argv[])
{
    int sock;                        /* Socket descriptor */
    struct sockaddr_in echoServAddr; /* Echo server address */
    struct sockaddr_in fromAddr;     /* Source address of echo */
    unsigned short echoServPort;     /* Echo server port */
    unsigned int fromSize;           /* In-out of address size for recvfrom() */
    char *servIP;                    /* IP address of server */
    int nBytes;              		 /* Length of received response */

	struct sample example;

    if (argc < 3)    /* Test for correct number of arguments */
    {
        fprintf(stderr,"Usage: %s <Server IP address> <Echo Port>\n", argv[0]);
        exit(1);
    }

    servIP = argv[1];           /* First arg: server IP address (dotted quad) */
    echoServPort = atoi(argv[2]);  /* Second arg: Use given port, if any */

	printf( "Arguments passed: server IP %s, port %d\n", servIP, echoServPort );

    /* Create a datagram/UDP socket */

    if ((sock = socket(PF_INET, SOCK_DGRAM, IPPROTO_UDP)) < 0)
        DieWithError("socket() failed");

    /* Construct the server address structure */

    memset(&echoServAddr, 0, sizeof(echoServAddr));    /* Zero out structure */
    echoServAddr.sin_family = AF_INET;                 /* Internet addr family */
    echoServAddr.sin_addr.s_addr = inet_addr(servIP);  /* Server IP address */
    echoServAddr.sin_port   = htons(echoServPort);     /* Server port */

	/* Pass string back and forth between server 5 times */

	printf( "Echoing %d iterations.\n", ITERATIONS );

	example.n = 1;

	for( int i = 0; i < ITERATIONS; i++ )
	{
		strcpy( example.message, "Request" );
		printf( "\nClient sending <message,n> in struct to: <%s,%d>\n", example.message, example.n );

    	/* Send the struct to the server */

    	if (sendto(sock, &example, sizeof(struct sample), 0, (struct sockaddr *) &echoServAddr, sizeof(echoServAddr)) != sizeof(struct sample))
       		DieWithError("sendto() sent a different number of bytes than expected");

    	/* Receive a response */

   		fromSize = sizeof(fromAddr);

   		if ((nBytes = recvfrom(sock, &example, sizeof(struct sample), 0, (struct sockaddr *) &fromAddr, &fromSize)) > sizeof(struct sample) )
       		DieWithError("recvfrom() failed");

   		if (echoServAddr.sin_addr.s_addr != fromAddr.sin_addr.s_addr)
   		{
       			fprintf(stderr,"Error: received a packet from unknown source.\n");
       			exit(1);
   		}

 		printf("\nClient received message from server: ``%s''\n", example.message );    /* Print the echoed arg */
 		printf("Client received value n from server: %d\n", example.n );    /* Print the echoed arg */
 
	}
    
    close(sock);
    exit(0);
}
