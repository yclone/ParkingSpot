package test

import (
	"testing"
	"github.com/gruntwork-io/terratest/modules/terraform"
	"github.com/gruntwork-io/terratest/modules/aws"
	"github.com/stretchr/testify/assert"
)

func TestVPCConfiguration(t *testing.T) {
	terraformOptions := &terraform.Options{
		TerraformDir: "..",
		Vars: map[string]interface{}{
			"project_name": "tr-ai-test",
			"environment": "test",
		},
	}

	defer terraform.Destroy(t, terraformOptions)
	terraform.InitAndApply(t, terraformOptions)

	vpcId := terraform.Output(t, terraformOptions, "vpc_id")
	
	// Verify VPC exists
	vpc := aws.GetVpcById(t, vpcId, "us-east-1")
	assert.Equal(t, "10.0.0.0/16", vpc.CidrBlock)

	// Verify subnets
	subnets := aws.GetSubnetsForVpc(t, vpcId, "us-east-1")
	assert.Equal(t, 4, len(subnets)) // 2 public + 2 private subnets
}
