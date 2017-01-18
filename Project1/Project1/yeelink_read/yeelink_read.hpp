#ifndef __YEELINK_READ_
#define __YEELINK_READ_

#include <Winsock2.h>
#include <string>
#include <stdio.h>
#include <iostream>
#include <sstream>
#include "json\json.hpp"

class YEELINK_READ
{
public:
	YEELINK_READ();
	~YEELINK_READ();
	static double read_lastvalue(int device_id, int sensor_id);
	
private:
	static std::string read_lastdata(int device_id, int sensor_id);
};

YEELINK_READ::YEELINK_READ()
{
}

YEELINK_READ::~YEELINK_READ()
{
}

double YEELINK_READ::read_lastvalue(int device_id, int sensor_id) {
	double result = -1.0;
	std::string str;
	do {
		str = read_lastdata(device_id, sensor_id);
	} while (str.empty());

	try {
		nlohmann::json jj = nlohmann::json::parse(str.c_str());
		/*for (json::iterator it = j3.begin(); it != j3.end(); ++it) {
		std::cout << it.key() << " : " << it.value() << "\n";
		}*/
		result = jj["value"];
	}
	catch(char*){}
	return result;
}

std::string YEELINK_READ::read_lastdata(int device_id, int sensor_id) {
	std::string result;
	std::stringstream ss, sss;

	std::string sRemoteFilePath = "http://api.yeelink.net/v1.0/device/";
	std::string device;
	ss << device_id;
	ss >> device;
	sRemoteFilePath += device;
	sRemoteFilePath += "/sensor/";
	std::string sensor;
	sss << sensor_id;
	sss >> sensor;
	sRemoteFilePath += sensor;
	sRemoteFilePath += "/datapoints";
	std::string sRemoteIP = "api.yeelink.net";
	u_short nRemotePort = 80;

	try
	{
		WORD wVersionRequested = MAKEWORD(1, 1);
		WSADATA wsaData;
		int nRet;
		nRet = WSAStartup(wVersionRequested, &wsaData);
		if (nRet)
		{
			char ermsg[1024] = { 0 };
			sprintf_s(ermsg, "download %s,WSAStartup() error,error code : %d", sRemoteFilePath.c_str(), nRet);
			throw ermsg;
		}

		if (wsaData.wVersion != wVersionRequested)
			throw "WinSock version not supported";

		SOCKET Socket;

		Socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
		if (Socket == INVALID_SOCKET)
		{
			char ermsg[1024] = { 0 };
			sprintf_s(ermsg, "download %s,socket() error,error code : %d", sRemoteFilePath.c_str(), WSAGetLastError());

			throw ermsg;
		}

		// Find the port number for the HTTP service on TCP 
		SOCKADDR_IN saServer;
		saServer.sin_port = htons(nRemotePort);
		saServer.sin_family = AF_INET;
		saServer.sin_addr.s_addr = inet_addr(sRemoteIP.c_str());

		nRet = connect(Socket, (LPSOCKADDR)&saServer, sizeof(SOCKADDR_IN));
		if (nRet == SOCKET_ERROR)
		{
			HOSTENT* pHS = gethostbyname(sRemoteIP.c_str());
			if (pHS != NULL)
			{
				in_addr addr;
				CopyMemory(&addr.S_un.S_addr, pHS->h_addr_list[0], pHS->h_length);
				saServer.sin_addr.S_un.S_addr = addr.S_un.S_addr;
			}

			nRet = connect(Socket, (LPSOCKADDR)&saServer, sizeof(SOCKADDR_IN));

			if (nRet == SOCKET_ERROR) {
				char ermsg[1024] = { 0 };
				sprintf_s(ermsg, "download %s,connect() error,error code : %d", sRemoteFilePath.c_str(), WSAGetLastError());
				closesocket(Socket);
				throw ermsg;
			}
		}

		// Format the HTTP request 
		char szBuffer[102400];

		sprintf_s(szBuffer, "GET %s\n", sRemoteFilePath.c_str());
		nRet = send(Socket, szBuffer, strlen(szBuffer), 0);
		if (nRet == SOCKET_ERROR)
		{
			char ermsg[1024] = { 0 };
			sprintf_s(ermsg, "download %s,send() error,error code : %d", sRemoteFilePath.c_str(), WSAGetLastError());
			closesocket(Socket);
			throw ermsg;
		}


		while (1)
		{
			char szBuffer[102400];
			memset(szBuffer, 0, sizeof(szBuffer));
			nRet = recv(Socket, szBuffer, sizeof(szBuffer), 0);
			if (nRet == SOCKET_ERROR)
			{
				char ermsg[1024] = { 0 };
				sprintf_s(ermsg, "download %s,recv() error,error code : %d", sRemoteFilePath.c_str(), WSAGetLastError());
				closesocket(Socket);
				throw ermsg;
			}

			if (nRet == 0)
				break;

			result += szBuffer;
		}

		closesocket(Socket);
		WSACleanup();
	}
	catch (char* sErrMsg)
	{
		printf("error : %s\n",sErrMsg);

		WSACleanup();
	}

	return result;

}



#endif // !__YEELINK_READ_



