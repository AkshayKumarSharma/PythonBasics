import configparser
import ConfigurationReader

configReader = ConfigurationReader.ConfigurationReader()
listOfIpParts = configReader.FetchValue('DEFAULT','HostIp').split(':')

for f in listOfIpParts:
    intIpPart = int(f)
    print(intIpPart)
    # print(type(intIpPart))
    print(f'Converted type :  {type(intIpPart)} for actual type :  {type(f)}')

print(listOfIpParts)