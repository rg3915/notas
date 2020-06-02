<template>
  <div>
    <b-container>
      <div class="float-right pb-3">
        <b-button variant="primary" @click="isModalVisible = true">Adicionar usuário</b-button>
      </div>
    </b-container>

    <b-container>
      <b-table class="mt-3" striped hover :fields="fields" :items="users">
        <template v-slot:cell(actions)="row">
          <b-button size="sm" @click="editUser(row.item)" variant="primary" class="mr-1">
            Editar
          </b-button>
          <b-button size="sm" @click="deleteUser(row.item)" variant="danger">
            Apagar
          </b-button>
        </template>
      </b-table>
    </b-container>

    <b-modal
      :title="editingUser.pk ? 'Editar usuário' : 'Adicionar usuário'"
      @ok="sendUser"
      @hidden="editingUser = {}"
      v-model="isModalVisible"
    >
      <b-form-group
        label="Nome"
        label-for="name"
      >
        <b-form-input id="name" type="text" v-model="editingUser.name"></b-form-input>
      </b-form-group>
      
      <b-form-group
        label="Nota 1"
        label-for="grade1"
      >
        <b-form-input id="grade1" type="number" v-model="editingUser.grade1"></b-form-input>
      </b-form-group>
      
      <b-form-group
        label="Nota 2"
        label-for="grade2"
      >
        <b-form-input id="grade2" type="number" v-model="editingUser.grade2"></b-form-input>
      </b-form-group>
    </b-modal>
  </div>
</template>
<script>
import axios from 'axios'

const endpoint = 'http://localhost:8000/'

export default {
  data() {
    return {
      users: [],
      editingUser: {},
      isModalVisible: false,
      fields: [{
        label: 'Nome',
        key: 'name'
      }, {
        label: 'Nota 1',
        key: 'grade1'
      }, {
        label: 'Nota 2',
        key: 'grade2'
      }, {
        label: 'Ações',
        key: 'actions'
      }]
    }
  },
  created() {
    axios.get(endpoint + 'grade/')
      .then(response => {
        this.users = response.data;
      })
  },
  methods: {
    sendUser() {
      const { id } = this.editingUser;

      if (id) {
        axios.put(endpoint + 'grade/' + id + '/', this.editingUser)
          .then(res => {
            const users = [...this.users];
            const index = users.findIndex(u => u.id == id);
            users[index] = res.data;
            this.users = users;
          });
        return;
      }

      axios.post(endpoint + 'grade/', this.editingUser)
        .then(res => {
          this.users.push(res.data);
        });
    },
    editUser(user) {
      this.editingUser = { ...user };
      this.isModalVisible = true;
    },
    deleteUser(user) {
      if (!confirm('Tem certeza que deseja remover este usuário?')) {
        return;
      }

      axios.delete(endpoint + 'grade/' + user.id + '/')
        .then(() => {
          const users = this.users.filter(u => u.id != user.id);
          this.users = users;
        });
    },
  }
}
</script>
