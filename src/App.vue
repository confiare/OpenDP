<template>
<div id="app">
  <v-app id="inspire">
    <v-stepper v-model="e6" vertical>
      <v-stepper-step :complete="e6 > 1" step="1">
        Introduction
        <small>Welcome to WhiteNoise, a tool that helps generate statistics (such as means or histograms) that are privacy preserving by distributing a "privacy budget" across different calculations.</small>
      </v-stepper-step>
      <v-stepper-content step="1">
        <v-card class="mb-12" color="grey lighten-1" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 2">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 2" step="2">Import Data</v-stepper-step>
      <v-stepper-content step="2">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 3">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 3" step="3">
	Import Data
	<small>Upload dataset</small>
      </v-stepper-step>
      <v-stepper-content step="3">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 4">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 4" step="4">
	Import Data
	<small>Confirm dataset</small>
      </v-stepper-step>
      <v-stepper-content step="4">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 5">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 5" step="5">
	Import Data
	<small>Select dataset type</small>
      </v-stepper-step>
      <v-stepper-content step="5">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 6">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 6" step="6">
	Import Data
	<small>Confirm contents of dataset</small>
      </v-stepper-step>
      <v-stepper-content step="6">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 7">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 7" step="7">
	Import Data
	<small>Specify dataset information</small>
      </v-stepper-step>
      <v-stepper-content step="7">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 8">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 8" step="8">Specify Metadata</v-stepper-step>
      <v-stepper-content step="8">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 9">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 9" step="9">
	Specify Metadata
	<small>Create custom variables</small>
      </v-stepper-step>
      <v-stepper-content step="9">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 10">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 10" step="10">
	Specify Metadata
	<small>Confirm variable types</small>
      </v-stepper-step>
      <v-stepper-content step="10">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 11">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 11" step="11">
	Specify Metadata
	<small>Set variable ranges</small>
      </v-stepper-step>
      <v-stepper-content step="11">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 12">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 12" step="12">
	Specify Metadata
	<small>Confirm variables of interest</small>
      </v-stepper-step>
      <v-stepper-content step="12">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 13">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 13" step="13">Set Parameters</v-stepper-step>
      <v-stepper-content step="13">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 14">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step step="14">
	Set Parameters
	<small>Set privacy loss parameters</small>
      </v-stepper-step>
      <v-stepper-content :complete="e6 > 14" step="14">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 15">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 15" step="15">Create Statistics</v-stepper-step>
      <v-stepper-content step="15">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 16">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 16" step="16">
	Create Statistics
	<small>Create Statistics</small>
      </v-stepper-step>
      <v-stepper-content step="16">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 17">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 17" step="17">Generate Report</v-stepper-step>
      <v-stepper-content step="17">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 18">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 18" step="18">
	Generate Report
	<small>Confirm error and submit</small>
      </v-stepper-step>
      <v-stepper-content step="18">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 19">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step :complete="e6 > 19" step="19">
	Generate Report
	<small>View report</small>
      </v-stepper-step>
      <v-stepper-content step="19">
        <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
        <v-btn color="primary" @click="e6 = 1">Continue</v-btn>
        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
    </v-stepper>
  </v-app>
</div>
</template>
<script>
  export default {
    data () {
      return {
        e6: 1,
      }
    },
  }
</script>
<style>
</style>

