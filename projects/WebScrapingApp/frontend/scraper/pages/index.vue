<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card>
        <v-card-title class="headline">
          This is an app designed to study team development
        </v-card-title>
        <v-card-text>
          <p>You can know popular news in Yahoo! News</p>
          <div class="text-xs-right">
            <em><small>&mdash; virtual-hippo, c1228j</small></em>
          </div>

          <hr class="my-3">
          
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn
            color="primary"
            nuxt
            to="/search"
          >
            Continue
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'IndexPage'
}
</script>
