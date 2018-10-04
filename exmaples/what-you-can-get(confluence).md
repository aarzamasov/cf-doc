h3. Parameters

||#||Name||Default Value||Description||
| 1 | EnvType | stage | Env Type of ElasticCache |
| 2 | VPCName |  | The Name of VPC |
| 3 | RetentionPeriod |  |  |
| 4 | ShardCount |  |  |

h3. Resources

||#||Resource||Name||Description||
| 1 | Lambda Function |OutputKinesisStream |  |
| 2 | Kinesis Stream |InputKinesisStream |  |
| 3 | Kinesis Analytics Application |BasicApplication |  |
| 4 | IAM Role |KinesisAnalyticsRole |  |
| 5 | IAM Role |LambdaRole |  |