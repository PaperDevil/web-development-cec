<template>
  <div v-if="isDelete" class="TodoItem">
    <div v-if="showDelete" class="" v-show="needToShow">
      <input
        class="input-check"
        type="checkbox"
        name="complete"
        v-model="isComplete"
        id=""
      />
      <h4 v-if="isComplete" style="text-decoration: line-through">{{ msg }}</h4>
      <h4 v-else>{{ msg }}</h4>
      <input type="button" value="Восстановить" @click="deleteOrRetore()" />
    </div>
  </div>
  <div v-else class="TodoItem" v-show="needToShow">
    <input
      class="input-check"
      type="checkbox"
      name="complete"
      v-model="isComplete"
      id=""
    />
    <h4 v-if="isComplete" style="text-decoration: line-through">{{ msg }}</h4>
    <h4 v-else>{{ msg }}</h4>
    <input type="button" value="Удалить" @click="deleteOrRetore()" />
  </div>
</template>

<script>
export default {
  name: "TodoItem",
  props: ["msg", "showDelete", "hideComplete"],
  data: function () {
    return {
      isComplete: false,
      isDelete: false,
    };
  },
  methods: {
    deleteOrRetore() {
      if (this.isDelete) {
        console.log(`Восстановление элемента с именем ${this.msg}`);
      } else {
        console.log(`Удаление элемента с именем ${this.msg}`);
      }
      this.isDelete = !this.isDelete;
    },
  },
  computed: {
    needToShow() {
      console.log(this.hideComplete);
      return !(this.isComplete && this.hideComplete);
    },
  },
};
</script>

<style lang="stylus" scoped>
.TodoItem {
  display: flex;
  flex-direction: row;
  text-align: center;
  vertical-align: center;
  justify-content: middle;
  border: 1px solid black;
  padding: 3px;
}

.input-check {
  margin-right: 15px;
}
</style>