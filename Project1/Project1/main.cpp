#define _WINSOCK_DEPRECATED_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <Winsock2.h>
#include <string>
#include <iostream>

#include "yeelink_read\yeelink_read.hpp"


#pragma comment(lib, "ws2_32.lib")

using namespace std;







int main()
{
	//GetHTTP("42.96.164.52", 80, "http://api.yeelink.net/v1.0/device/353097/sensor/397985.json?start=2012-06-02T14:01:46&end=2017-06-15T15:21:40&interval=1&page=1", "data.dat");

	//string str = GetHTTP("api.yeelink.net", 80, "http://api.yeelink.net/v1.0/device/353097/sensor/397985/datapoints");

	double d1s1 = YEELINK_READ::read_lastvalue(353097, 397985);
	cout << d1s1 << endl;

	system("pause");
	return 0;
}