package test

import (
	"testing"
	"github.com/gruntwork-io/terratest/modules/terraform"
	"github.com/stretchr/testify/assert"
)

func TestTerraformInfrastructure(t *testing.T) {
	terraformOptions := &terraform.Options{
		// The path to where your Terraform code is located
		TerraformDir: "..",
		
		// Variables to pass to our Terraform code using -var options
		Vars: map[string]interface{}{
			"project_name": "tr-ai-test",
			"environment": "test",
		},
	}

	// At the end of the test, run `terraform destroy`
	defer terraform.Destroy(t, terraformOptions)

	// Run `terraform init` and `terraform apply`
	terraform.InitAndApply(t, terraformOptions)

	// Verify that the VPC was created with the correct CIDR
	vpcId := terraform.Output(t, terraformOptions, "vpc_id")
	assert.NotEmpty(t, vpcId)

	// Verify that the ECR repository URL was created
	ecrRepositoryUrl := terraform.Output(t, terraformOptions, "ecr_repository_url")
	assert.NotEmpty(t, ecrRepositoryUrl)

	// Verify that the ALB DNS name was created
	albDnsName := terraform.Output(t, terraformOptions, "alb_dns_name")
	assert.NotEmpty(t, albDnsName)
}
