# here libraries/classe are imported
import configparser # this one is python's own class
import ConfigurationReader # this is custom created, for possible re-use at later stage
import Features.DataTypes

# initialized an instance of ConfigurationReader class
configReader = ConfigurationReader.ConfigurationReader()
ipAddress = configReader.FetchValue('DEFAULT','IPAddress')
splittedIpAddress = ipAddress.split(':') # here the ip address is split on the basis of ':'

# here ip address from config file will be printed
print(f'Ip address from config file : {ipAddress}')

# here splitted list will be printed
print(splittedIpAddress)

# here basic for loop is demonstrated, in addition to type casting
for splitPart in splittedIpAddress: 
    convertedToInt = int(splitPart)
    print(f'Converted type :  {type(convertedToInt)} for actual type :  {type(splitPart)}')


dataTypeExamples = Features.DataTypes.DataTypeExamples()
dataTypeExamples.PrintDataTypes()


