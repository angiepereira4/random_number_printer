# Case Study  
Imagine a server with the following specs:  
● 4 times Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz  
● 64GB of ram  
● 2 TB HDD disk space  
● 2 x 10Gbit/s nics  
The server is used for SSL offloading and proxies around 25000 requests per second.   
Please let us know which metrics are interesting to monitor in that specific case and how would you do that? What are the challenges of monitoring this?  

## Analysis  
In this scenario, there are several metrics that are interesting to monitor to ensure the server is performing optimally and efficiently. Here are some of the most critical ones that I would consider to monitor mainly :  

# CPU Utilization
Since the above mentioned server is using four Intel Xeon CPUs, monitoring their usage can help determine if the processing power is sufficient to handle the incoming requests. Monitoring CPU usage can also help identify any spikes or anomalies that may indicate a problem with the server. We can also create an alert in graphical monitoring tools like DataDog/grafana fetching the metrics and specifying thresholds if it crosses a specific maximum point to alert us and hence be actionable from our side immediately.System monitoring tools such as top, htop, or Glances to monitor CPU and memory usage.  
We can follow the below steps :  
1. Use a **monitoring tool**: Use a monitoring tool like Prometheus, Zabbix, or Nagios to monitor the CPU utilization of the server. These tools can provide you with metrics such as CPU usage, CPU load, CPU temperature, and other relevant information.  
2. Use a **system monitoring tool**: Use a system monitoring tool like top or htop to monitor the CPU utilization of the server in real-time. These tools can provide you with information on the percentage of CPU usage, CPU load, and other metrics.  
3. Monitor individual **CPU cores**: The Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz has 14 cores per processor, so a total of 56 cores in the server. It is important to monitor the utilization of individual CPU cores as well as the overall CPU utilization. Tools like mpstat or sar can provide you with information on the utilization of individual CPU cores.  
4. Set up **alerts**: Set up alerts to notify you when the CPU utilization exceeds a certain threshold. You can use tools like PagerDuty, Slack, or Email alerts to receive notifications when the CPU utilization reaches a certain level. This will help you to take immediate action and prevent potential downtime.  
5. Check for **CPU throttling**: Check if CPU throttling is occurring on the server. CPU throttling occurs when the CPU frequency is reduced due to overheating or other issues. Tools like lm-sensors can be used to monitor the temperature of the CPU and other components on the server.

# Memory Utilization  
The server has 64GB of RAM, which is a considerable amount of memory. Monitoring memory usage can help identify any potential memory leaks or issues with memory allocation that may affect the server's performance. We can use a performance monitoring tool such as Nagios, Zabbix, or Prometheus can be used to monitor memory utilization over time. We can collect and analyze metrics and provide a graphical representation of memory usage, making it easier to identify trends and potential issues. As mentioned above System monitoring tools such as top, htop, or Glances to monitor CPU and memory usage, we can also use the "free" command to display the amount of free and used memory in the system. 
We can follow the below steps:  
1. Use a **monitoring tool**: Use a monitoring tool like Prometheus, Zabbix, or Nagios to monitor the memory utilization of the server. These tools can provide you with metrics such as memory usage, memory available, swap usage, and other relevant information.  
2. Use a **system monitoring** tool: Use a system monitoring tool like top or htop to monitor the memory utilization of the server in real-time. These tools can provide you with information on the percentage of memory usage, memory available, and other metrics.  
3. Monitor **individual processes**: Monitor the memory utilization of individual processes running on the server. Tools like ps or top can provide you with information on the memory usage of individual processes. This will help you to identify any memory-hogging processes that may be impacting server performance.  
4. Set up **alerts**: Set up alerts to notify you when the memory utilization exceeds a certain threshold. You can use tools like PagerDuty, Slack, or Email alerts to receive notifications when the memory utilization reaches a certain level. This will help you to take immediate action and prevent potential downtime.  
5. Check for **memory leaks**: Check if any processes on the server are experiencing memory leaks. Memory leaks occur when a process continually allocates memory without releasing it, leading to a gradual increase in memory usage over time. Tools like Valgrind or GDB can be used to identify and fix memory leaks.  


# Disk space Utilization  
The server has a 2TB HDD disk space, which may fill up quickly depending on the amount of data being stored. Monitoring disk space usage can help ensure that the server doesn't run out of space, which could lead to data loss and other issues.We can hence create an alert in a performance monitoring tool like Zabbix/Datadog with a threshold to make sure that Disk space consumption is always under the limit , and hence if it goes above the threshold we could implement a script to clear disk space or manually log(ssh) into the respective server and clear tmp files or any other unwanted files which are eating up alot of disk space. We can use Filesystem monitoring such as df, du, or iostat to monitor disk space usage.
We can follow the below steps:  
1. Use a **monitoring tool**: Use a monitoring tool like Prometheus, Zabbix, or Nagios to monitor the disk utilization of the server. These tools can provide you with metrics such as disk space usage, disk I/O, and other relevant information.  
2. Use a **system monitoring tool**: Use a system monitoring tool like df or du to monitor the disk utilization of the server in real-time. These tools can provide you with information on the amount of disk space used and the amount of free disk space available.  
3. Monitor **individual directories**: Monitor the disk utilization of individual directories on the server. Tools like du or ncdu can provide you with information on the disk usage of individual directories. This will help you to identify any directories that may be consuming a significant amount of disk space.  
4. Set up **alerts**: Set up alerts to notify you when the disk utilization exceeds a certain threshold. You can use tools like PagerDuty, Slack, or Email alerts to receive notifications when the disk utilization reaches a certain level. This will help you to take immediate action and prevent potential downtime.  
5. Check for **disk errors**: Check for disk errors that may be impacting server performance. Tools like smartctl can be used to check for disk errors and monitor disk health.  


# Network Utilization  
The server has 2 x 10Gbit/s nics, which means that it can handle a lot of network traffic. Monitoring network usage can help determine if the server is reaching its maximum capacity, and if there are any bottlenecks in the network.Network monitoring tools such as tcpdump, wireshark, or ntopng to monitor network usage and SSL connections. We can also use Log Monitor to monitor the network devices in a network including the switches,routers, primary or secondary circuits.  
We can follow the below steps:  
1. Use a monitoring tool: Use a monitoring tool like Prometheus, Zabbix, or Nagios to monitor the network utilization of the server. These tools can provide you with metrics such as network traffic, packets transmitted and received, and other relevant information.  
2. Use a system monitoring tool: Use a system monitoring tool like iftop or iptraf to monitor the network utilization of the server in real-time. These tools can provide you with information on the amount of network traffic, the number of packets transmitted and received, and other metrics.  
3. Monitor individual connections: Monitor the network utilization of individual connections on the server. Tools like netstat or lsof can provide you with information on active network connections and the amount of traffic associated with each connection. This will help you to identify any connections that may be consuming a significant amount of network bandwidth.  
4. Set up alerts: Set up alerts to notify you when the network utilization exceeds a certain threshold. You can use tools like PagerDuty, Slack, or Email alerts to receive notifications when the network utilization reaches a certain level. This will help you to take immediate action and prevent potential downtime.  
5. Monitor network errors: Monitor the network for errors that may be impacting server performance. Tools like ethtool can be used to check for network errors and monitor network health.  
By following these steps, we can effectively monitor the network utilization of your bare metal server used for SSL offloading and proxies around 25000 requests per second with 2 x 10Gbit/s nics, and ensure optimal performance and uptime.


# SSL Connections
Since the server is used for SSL offloading, monitoring SSL connections can help ensure that the server is handling SSL traffic correctly and that there are no issues with SSL certificate validation.We can also create alerts in Datadog for example for SSL cert expiration , and place the alert on warning before "N" number of days before expiration so that we can renew the the SSL certs way in advance instead of waiting for it till it expires.  
We can follow the below steps :  
1. Use a **monitoring tool**: Use a monitoring tool like Prometheus, Zabbix, or Nagios to monitor the SSL connections of the server. These tools can provide you with metrics such as the number of SSL connections, the number of failed SSL connections, SSL handshake time, SSL session cache hits and misses, SSL errors, and other relevant information.    
2. Enable **SSL logging**: Enable SSL logging in your web server configuration to log SSL-related events. This will help you to track down any SSL-related issues that may occur. You can use the logs to identify the source of SSL connection problems and take appropriate measures to fix them.  
3. Monitor **CPU and Memory usage**: Monitoring the CPU and memory usage of your server is crucial to ensuring optimal performance. We can use tools like top or htop to monitor CPU and memory usage. Make sure to monitor the server's resources regularly to ensure that they are not being overused, which could lead to server downtime.  
4. Use **network monitoring tools**: Use network monitoring tools like Wireshark or tcpdump to capture and analyze network traffic on the server. This will help you to detect any unusual network activity, identify bottlenecks in the SSL offloading process, and troubleshoot network-related issues.  
5. Set up **alerts**: Set up alerts to notify you when there is an SSL-related issue or when resource usage exceeds a certain threshold. You can use tools like PagerDuty, Slack, or Email alerts to receive notifications when an issue arises. This will help you to take immediate action and prevent potential downtime.  
By following these steps, you can effectively monitor the SSL connections of your bare metal server used for SSL offloading and proxies around 25000 requests per second and ensure optimal performance and uptime.  
