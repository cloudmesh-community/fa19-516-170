# Datacenter fa19-516-170

## E.Datacenter.2.a

### Lakeside Technology Center - Chicago, IL

|Electricity Cost | IT Load | Yearly Cost ($) | Yearly CO2 Footprint (tons) | CO2 equivalent in cars |
|----|----|----|----|----|
| $0.15/kWh |	100,000 kW | $131.4M | 670,140 metric tons |  147,736 cars|

Assuming the data center works 24/7 at 100 MW, then resulting in 876,000,000 kWh per year, 
\
CO2 footprint: avg 1.7 lbs/kWh.
\
Yearly Cost is calculated based on electricity cost and IT Load.

## E.Datacenter.2.b
The Lakeside Technology Center (350 East Cermak) is a 1.1 million square foot multi-tenant 
data center hub  owned by Digital Realty Trust. Originally developed by the R.R. Donnelley Co. 
to house the printing presses for the Yellow Book and Sears Catalog, 
350 East Cermak was converted to telecom use in 1999, and today it is one of the world’s largest 
carrier hotels and the nerve center for Chicago’s commodity markets, housing data centers for 
financial firms attracted by the wealth of peering and connectivity providers among the 70 tenants.

The industrial strength infrastructure includes four fiber vaults and three electric power feeds, which provide the building with more than 100 megawatts of power. 

One of the most distinctive features of the facility is its cooling system, which is supported by an 8.5 million gallon tank of a refrigerated brine-like liquid. The huge tank serves as thermal energy storage for the Metropolitan Pier and Exposition Authority (MPEA), including the nearby McCormick Place Exposition Center and Hyatt Regency Hotel as well as 350 East Cermak. Thermal energy storage can reduce costs by running chillers during off-peak hours when power rates are cheaper.

*References*

[Strange Marriage by the Lake](http://www.progressiveengineer.com/PEWebBackissues2004/PEWeb%2048%20Mar%2004-2/Lakeside.htm/)  
[Digital Realty- Lakeside](http://worldstopdatacenters.com/digital-realty-lakeside/)  
[Massive South Loop data center ready for expansion](https://www.chicagobusiness.com/article/20161020/CRED03/161029995/one-of-world-s-largest-data-centers-expanding-in-south-loop/)  
[World's Largest Data Center: 350 E. Cermak](https://www.datacenterknowledge.com/special-report-the-worlds-largest-data-centers/worlds-largest-data-center-350-e-cermak/)  
[Chicago's Data Fortress for the Digital Economy](https://www.datacenterknowledge.com/archives/2009/01/06/chicagos-data-fortress-for-the-digital-economy)

## E.Datacenter.3
12343 LBS of CO2, 5834 LBS comes from home.

## E.Datacenter.4
Solar power is energy from the sun that is converted into thermal or electrical energy. Solar energy is the cleanest and most abundant renewable energy source available, and the U.S. has some of the richest solar resources in the world. Solar technologies can harness this energy for a variety of uses, including generating electricity, providing light or a comfortable interior environment, and heating water for domestic, commercial, or industrial use.

According to [Solor-Powered Data Centers](https://www.datacenterknowledge.com/solar-powered-data-centers), 
solor power hasn't been widely used in data centers because a decent amount of energy required by data centers
demands a very large installation of photovoltaic(PV). However, there are still some data centers that 
successfully implements solar power. For example, AISO is a nature intended web hosting company. It claimed 
that "Every hosting account with AISO is green and powered by on-site solar". Due to this philosophy, the company eliminate the production of 34488 lbs of co2 per year.

*References*

[Solor-Powered Data Centers](https://www.datacenterknowledge.com/solar-powered-data-centers/)  
[AISO](https://www.aiso.net/)

## E.Datacenter.5
According to [China's data centers emit as much carbon as 21 million cars](https://www.cnn.com/2019/09/10/asia/china-data-center-carbon-emissions-intl-hnk/index.html),
China's data centers produced 99 million metric tons of carbon dioxide in 2018, which is equivalent to about 21 million 
cars on the road. And the article also anticipates that co2 emission will climb to 163 million metric tons, which is equivalent 
to 35 million cars. To reduce the amount of co2 emission produced by data centers, China's data centers take actions to
decouple their electricity consumption from their carbon footprint by relying more on wind and solar energy. In 2015, Chinese 
government launched a green data center pilot program. In the same year, one of China's largest cloud computing providers--Alibaba 
started a data center located in Hangzhou, relying on solar and water energy. With the use of renewable energy, Chinese data centers combines the 
best of natural resources with modern city and advanced technology. Moreover, operational efficiency in the delievery of cloud computing 
and big data services is improved by the smart use of renewable energy.

*References*

[China's data centers emit as much carbon as 21 million cars](https://www.cnn.com/2019/09/10/asia/china-data-center-carbon-emissions-intl-hnk/index.html)  
[AliCloud Launches New Energy-Efficient Qiandao Lake Data Center](https://www.businesswire.com/news/home/20150908005493/en/AliCloud-Launches-New-Energy-Efficient-Qiandao-Lake-Data)

## E.Datacenter.8
### Disruption of Google Cloud Service

#### Incident
Google is one of the most widely-used and reliable service providers on the Internet. Once it experiences an outage, the consequences 
can be far-reaching. In June 2nd, 2019, Google experienced an outage.

According to [Google Cloud Networking Incident #19009](https://status.cloud.google.com/incident/cloud-networking/19009), The outage was initiated by two misconfigurations and a specific software bug, then leading to software maintenance events and resulting 
in network congestion. The congestion lasted for between 3 hours 19 minutes and 4 hours 25 minutes varied from region to region. Users who 
lives in eastern US were severely affected by the outage. Fortunately, most users who lives in western US and all the users in Europe and Asia 
were not affected. During the congestion, Google services including computing engine, App engine, cloud platform were disrupted.

#### Impact
According to [incident report](https://cloud.google.com/blog/topics/inside-google-cloud/an-update-on-sundays-service-disruption) YouTube measured a 2.5% drop of views for one hour, while Google Cloud Storage measured a 30% reduction in traffic. 
Approximately 1% of active Gmail users had problems with their account, which represents millions of users who couldn’t receive or send email.

#### Discussion
After the Google Outage, many people pays more attention to cloud network reliability. At the time cloud services are disrupted, 
people realizes these services have been an integral part of life, and the integral part of life relies on the ability of companies 
who manage these services to operate. Thus, people claim for cloud service should include reater dynamic visibility, more accountability and a better cost recovery plan when problems occur.

*References*

 [Google Cloud Networking Incident #19009](https://status.cloud.google.com/incident/cloud-networking/19009)  
 [An update on Sunday’s service disruption](https://cloud.google.com/blog/topics/inside-google-cloud/an-update-on-sundays-service-disruption)   
 [Google cloud is down, affecting numerous applications and services](https://techcrunch.com/2019/06/02/google-cloud-is-down-affecting-numerous-applications-and-services/)  
 [Latest Google Outage Impacted Way More Than Its Own Apps](https://www.forbes.com/sites/leemathews/2019/06/03/latest-google-outage-impacted-way-more-than-its-own-apps/#68b33f055ccd)  
 [Google Outage Sharpens Focus on Cloud Network Reliability](https://datacenterfrontier.com/google-outage-sharpens-focus-on-cloud-network-reliability/)  
 [Google’s Cloud outage reveals the holes in cloud computing’s atmosphere](https://techcrunch.com/2019/06/02/googles-cloud-outage-is-resolved-but-it-reveals-the-holes-in-cloud-computings-atmosphere/)


