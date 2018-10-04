import json

class GetMarkdown:

    def __init__(self,file_name, markdown_type):
        self.data = json.loads(open(file_name).read())
        self.parameters = []
        self.resources = []
        self.type_of_markdown = markdown_type


    def get_the_value(self, sibling, var, name_of_parameter):
        try:
            x = self.data[sibling][var][name_of_parameter]
        except:
            x = ''
            pass
        return x

    def get_value_from_properties_resource(self, sibling, var, name_of_parameter):
        try:
            x = self.data[sibling][var]['Properties'][name_of_parameter]
        except:
            x = ''
            pass
        return x


    def get_content_of_the_group(self, group_name):
        z =0
        content=[]

        if self.type_of_markdown == 'classic':
            content.append('### %s' % group_name)
            content.append('')
            if group_name == 'Parameters':
                content.append('|#|Name|Default Value|Description|')
                content.append('|-:|:---|:---------:|:------|')
            if group_name == 'Resources':
                content.append('|#|Resource|Name|Description|')
                content.append('|-:|:---|:---------|:------|')

        if self.type_of_markdown == 'confluence':
            content.append('h3. %s' % group_name)
            content.append('')
            if group_name == 'Parameters':
                content.append('||#||Name||Default Value||Description||')
            if group_name == 'Resources':
                content.append('||#||Resource||Name||Description||')

        for name in self.data[group_name]:
            z += 1
            if group_name == 'Parameters':
                default = self.get_the_value('Parameters', name, 'Default')
                desc = self.get_the_value('Parameters',name, 'Description')
                row = '| %s | %s | %s | %s |' % (z, name, default, desc)
            if group_name == 'Resources':
                desc = ''
                tp = self.get_the_value('Resources', name, 'Type')
                human_type, desc = self.get_the_human_type(tp, name)
                if tp == 'AWS::EC2::SecurityGroup':
                   desc = self.get_value_from_properties_resource('Resources', name, 'GroupDescription')
                if tp == 'AWS::CloudWatch::Alarm':
                   desc = self.get_value_from_properties_resource('Resources', name, 'AlarmDescription')
                row = '| %s | %s |%s | %s |' % (z, human_type, name, desc)


            content.append(row)
        content.append('')
        self.parameters = self.parameters+content

    def check_zone(self, name):
        visible = ['public', 'private']
        zones = ['a', 'b', 'c']
        z = ''
        for i in visible:
            if name.find(i) > -1:
                for j in zones:
                    if name.find('%s%s' %(i,j)) > -1 or name.find('%s%s' %(j,i)) > -1 :
                        z = j
                        break
                if z != '':
                    z = 'zone %s' % (z.upper())
                    break
        return z

    def get_the_human_type(self, tp, name):
        lower_name = name.lower()
        human_type = 'Undefined %s please check method get_the_human_type' % tp
        desc = ''
        visible = 'private'
        if lower_name.find('public') > -1:
            visible = 'public'
        zone = self.check_zone(lower_name)

        if tp == 'AWS::EC2::SubnetRouteTableAssociation':
            human_type = 'Route Table Association'
            desc = 'route table association for %s subnets %s' % (visible, zone)

        if tp == 'AWS::EC2::Route':
            human_type = 'Route Table'
            desc = 'route table for %s subnet %s' % (visible, zone)

        if tp == 'AWS::EC2::VPCGatewayAttachment':
            human_type = 'VPC Gateway'
            desc = 'Gateway to Internet'

        if tp == 'AWS::EC2::VPCGatewayAttachment':
            human_type = 'VPC Gateway'
            desc = 'gateway to Internet'

        if tp == 'AWS::EC2::Subnet':
            human_type = '%s subnet' % visible.capitalize()
            desc = '%s subnet %s' % (visible, zone)

        if tp == 'AWS::EC2::RouteTable':
            human_type = 'Route table'
            desc = 'Route table to %s' % (visible)

        if tp == 'AWS::EC2::EIP':
            human_type = 'Elastic IP'

        if tp == 'AWS::EC2::InternetGateway':
            human_type = 'Internet gateway'

        if tp == 'AWS::EC2::VPC':
            human_type = 'VPC'

        if tp == 'AWS::EC2::NatGateway':
            human_type = 'Nat gateway'

        if tp == 'AWS::EC2::SecurityGroup':
            human_type = 'Security Group'

        if tp == 'AWS::EC2::VPCPeeringConnection':
            human_type = 'Peering connection'

        if tp == 'AWS::EC2::Instance':
            human_type = 'EC2 instance'

        if tp == 'AWS::RDS::DBInstance':
            human_type = 'RDS DB instance'

        if tp == 'AWS::RDS::DBCluster':
            human_type = 'RDS Cluster'

        if tp == 'AWS::RDS::DBSubnetGroup':
            human_type = 'DB Subnet Group'

        if tp == 'AWS::RDS::DBClusterParameterGroup':
            human_type = 'DB Cluster Parameter Group'

        if tp == 'AWS::RDS::DBParameterGroup':
            human_type = 'DB Parameter Group'

        if tp == 'AWS::CloudWatch::Alarm':
            human_type = 'CloudWatch Alarm'

        if tp == 'AWS::AutoScaling::AutoScalingGroup':
            human_type = 'Auto Scaling Group'

        if tp == 'AWS::AutoScaling::LaunchConfiguration':
            human_type = 'Auto Scaling Launch Configuration'

        if tp == 'AWS::AutoScaling::ScalingPolicy':
            human_type = 'Auto Scaling Scaling Policy'

        if tp == 'AWS::ElasticLoadBalancingV2::LoadBalancer':
            human_type = 'Load Balancer'

        if tp == 'AWS::ElasticLoadBalancingV2::Listener':
            human_type = 'Load Balancer Litener'

        if tp == 'AWS::ElasticLoadBalancingV2::TargetGroup':
            human_type = 'Load Balancer Target Group'

        if tp == 'AWS::SQS::Queue':
            human_type = 'SQS Queue'

        if tp == 'AWS::SNS::Topic':
            human_type = 'SNS Topic'

        if tp == 'AWS::SNS::Subscription':
            human_type = 'SNS Subscription'

        if tp == 'AWS::ElastiCache::ReplicationGroup':
            human_type = 'ElastiCache Replication Group'

        if tp == 'AWS::ElastiCache::SubnetGroup':
            human_type = 'ElastiCache Subnet Group'


        if tp == 'AWS::Lambda::Function':
            human_type = 'Lambda Function'

        if tp == 'AWS::Kinesis::Stream':
            human_type = 'Kinesis Stream'

        if tp == 'AWS::KinesisAnalytics::Application':
            human_type = 'Kinesis Analytics Application'

        if tp == 'AWS::IAM::Role':
            human_type = 'IAM Role'

        return human_type, desc

    def print_md(self):
        try:
            for i in self.parameters:
                print i
        except:
            pass

        for i in self.resources:
            print i


a = GetMarkdown('/tmp/test/test.json', 'confluence')
a.get_content_of_the_group('Parameters')
a.get_content_of_the_group('Resources')

a.print_md()
