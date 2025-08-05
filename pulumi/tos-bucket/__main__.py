import pulumi
import pulumi_volcengine as volcengine

# 从 Pulumi 配置中获取 bucket_name，这个参数将由我们的平台在运行时提供
config = pulumi.Config()
bucket_name = config.require("bucket_name")

# 创建 TOS 存储桶
tos_bucket = volcengine.tos.Bucket("tos-bucket", bucket_name=bucket_name, acl="public-read")

# 导出 TOS 存储桶的名称
pulumi.export("bucket_name", tos_bucket.bucket_name)