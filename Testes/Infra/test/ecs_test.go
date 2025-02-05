package test

import (
	"testing"
	"github.com/gruntwork-io/terratest/modules/terraform"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/ecs"
	"github.com/stretchr/testify/assert"
)

func TestECSConfiguration(t *testing.T) {
	terraformOptions := &terraform.Options{
		TerraformDir: "..",
		Vars: map[string]interface{}{
			"project_name": "tr-ai-test",
			"environment": "test",
		},
	}

	defer terraform.Destroy(t, terraformOptions)
	terraform.InitAndApply(t, terraformOptions)

	sess := session.Must(session.NewSession(&aws.Config{
		Region: aws.String("us-east-1"),
	}))

	ecsClient := ecs.New(sess)

	// Verify ECS Cluster exists
	clusterName := "tr-ai-test-cluster"
	input := &ecs.DescribeClustersInput{
		Clusters: []*string{
			aws.String(clusterName),
		},
	}

	result, err := ecsClient.DescribeClusters(input)
	assert.NoError(t, err)
	assert.Equal(t, 1, len(result.Clusters))
	assert.Equal(t, clusterName, *result.Clusters[0].ClusterName)
}
