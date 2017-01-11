#define _WINSOCK_DEPRECATED_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <Winsock2.h>
#include <string>


#pragma comment(lib, "ws2_32.lib")

using namespace std;

//远程IP，port，要下载的文件的绝对路径，本地保存的绝对路径 
bool  GetHTTP(string sRemoteIP, u_short nRemotePort, string sRemoteFilePath, string sSavePath)
{
	try 
	{
		WORD wVersionRequested  = MAKEWORD(1,1);
	WSADATA wsaData;
	int nRet;
	nRet  = WSAStartup(wVersionRequested, &wsaData);
	if (nRet)
	{
		char ermsg[1024] = { 0 };
		sprintf_s(ermsg,"download %s,WSAStartup() error,error code : %d",sRemoteFilePath, nRet);
		throw ermsg;
	}

	if (wsaData.wVersion  != wVersionRequested)
		throw "WinSock version not supported";

	SOCKET Socket;

	Socket  = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (Socket  == INVALID_SOCKET)
	{
		char ermsg[1024] = { 0 };
		sprintf_s(ermsg,"download %s,socket() error,error code : %d", sRemoteFilePath,WSAGetLastError());

		throw ermsg;
	}

	// Find the port number for the HTTP service on TCP 
	SOCKADDR_IN saServer;
	saServer.sin_port  = htons(nRemotePort);
	saServer.sin_family  = AF_INET;
	saServer.sin_addr.s_addr  = inet_addr(sRemoteIP.c_str());

	nRet  = connect(Socket, (LPSOCKADDR)&saServer, sizeof(SOCKADDR_IN));
	if (nRet  == SOCKET_ERROR)
	{
		char ermsg[1024] = { 0 };
		sprintf_s(ermsg,"download %s,connect() error,error code : %d",sRemoteFilePath, WSAGetLastError());
		closesocket(Socket);
		throw ermsg;
	}

	// Format the HTTP request 
	char szBuffer[102400];

	sprintf_s(szBuffer, "GET %s\n", sRemoteFilePath.c_str());
	nRet  = send(Socket, szBuffer, strlen(szBuffer), 0);
	if (nRet  == SOCKET_ERROR)
	{
		char ermsg[1024] = { 0 };
		sprintf_s(ermsg,"download %s,send() error,error code : %d", sRemoteFilePath,WSAGetLastError());
		closesocket(Socket);
		throw ermsg;
	}

	FILE *fp ;
	int nError  = fopen_s(&fp,sSavePath.c_str(),"wb");
	if (nError)
	{
		char ermsg[10240] = { 0 };
		sprintf_s(ermsg,"save %s file error.", sSavePath.c_str());
		closesocket(Socket);
		throw ermsg;
	}

	while (1)
	{
		nRet  = recv(Socket, szBuffer, sizeof(szBuffer), 0);
		if (nRet  == SOCKET_ERROR)
		{
			char ermsg[1024] = { 0 };
			sprintf_s(ermsg,"download %s,recv() error,error code : %d",sRemoteFilePath, WSAGetLastError());
			closesocket(Socket);
			throw ermsg;
		}

		if (nRet  == 0)
			break;

		fwrite(szBuffer, nRet, 1, fp);
	}
	fclose(fp);
	closesocket(Socket);
	WSACleanup();
	}
		catch (char* sErrMsg)
	{
			printf("error\n");

		WSACleanup();
		return false;
	}

	return true;
}


void main()
{
	//GetHTTP("42.96.164.52", 80, "http://api.yeelink.net/v1.0/device/353097/sensor/397985.json?start=2012-06-02T14:01:46&end=2017-06-15T15:21:40&interval=1&page=1", "data.dat");
	GetHTTP("42.96.164.52", 80, "http://api.yeelink.net/v1.0/device/353097/sensor/397985/datapoints", "data.dat");
	
}