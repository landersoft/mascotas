<template lang="html">
    <div class="container">
        <div class="col text-left">
            <h2>Lista de Gatos</h2>
        </div>
        <div class="col-md-12">
            <b-table striped hover :items="gatos" :fields="fields">
                
            </b-table>
        </div>
        
     </div>
</template>

<script>
export default {
  data() {
    return {
      fields: [
        { key: "name", label: "Nombre" },
        { key: "rage", label: "Raza" },
        { key: "sexo", label: "Sexo" }
      ],
      gatos: []
    };
  }
};
</script>

