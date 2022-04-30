<template>
    <v-container>
        <v-row>
            <v-col
            class="d-flex"
            cols="6"
            sm="6">
                <v-text-field
                    label="search word"
                    :rules="rules"
                    hide-details="auto"
                    v-model="search_word"
                ></v-text-field>
            </v-col>
            <v-col
            class="d-flex"
            cols="6"
            sm="6">
                <v-text-field
                    label="search num"
                    hide-details="auto"
                    v-model.number="search_num"
                ></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col
            class="d-flex"
            cols="6"
            sm="6">
            <v-spacer />
            <v-btn
                color="primary"
                @click="search"
                v-bind:disabled="search_word.length == 0"
                nuxt
            >
                search
                <v-icon
                dark
                right
                >
                mdi-magnify
                </v-icon>
            </v-btn>
            </v-col>
        </v-row>
        <v-row justify="center">
            <v-simple-table dark v-if="news">
                <template v-slot:default>
                <thead>
                    <tr>
                    <th class="text-left">
                        Title
                    </th>
                    <th class="text-left">
                        URL
                    </th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                    v-for="item in news"
                    :key="item.title"
                    >
                    <td>{{ item.title }}</td>
                    <td>
                        <a v-bind:href="item.url">{{ item.url }}</a>
                    </td>
                    </tr>
                </tbody>
                </template>
            </v-simple-table>
            <div v-if="hasError">
                <p>Error</p>
                <p>{{ errorMessage }}</p>
            </div>
        </v-row>
    </v-container >
</template>

<script>
import axios from 'axios';
export default {
  name: 'InspirePage',
  data: () => ({
      search_word: "",
      search_num: 5,
      news: null,
      hasError: false,
      errorMessage: "",
      loading: true,
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 1) || 'Min 1 characters',
      ],
  }),
  methods: {
        search: function () {
            this.hasError = false;
            this.errorMessage = "";
            this.loading = true;
            this.news = null;
            axios.post('/sample_api/news/', {search_word: this.search_word, search_num: this.search_num})
            .then(function (response) {
                if (response.data) {
                    if (response.data.error) {
                        this.hasError = true;
                        this.errorMessage = response.data.error;
                    } else {
                        this.news = response.data;
                    }
                }
            }.bind(this))
            .catch(function (error) {
                this.hasError = true;
                this.errorMessage = error;
            }.bind(this))
            .finally(function () {
                this.loading = false;
            }.bind(this))
        },
    },
}
</script>
