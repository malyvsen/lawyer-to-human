<template>
  <div class="paper-document">
    <p class="document-text">
      <span>Sit voluptatem aliquid error corporis laborum sapiente sint. Labore ipsam doloribus ut aut alias placeat.</span>
      <span
        class="underlined"
      >Atque autem et odio totam labore neque ut. Error soluta iste tenetur quia voluptas debitis dolores.
        <SideTooltip></SideTooltip>
      </span>
      {{ content }}
    </p>
  </div>
</template>

<script>
import SideTooltip from "./SideTooltip.vue";
export default {
  data: () => ({
    content: `
        Repudiandae quisquam vel eveniet praesentium. Et velit nisi dolores ducimus.
        Corporis ratione unde at voluptatibus rerum sed fugit animi. Aut natus a ut est accusamus ullam animi voluptate.
        Nostrum officia animi aliquam quia pariatur ut odio.
        Quae sint vero reiciendis magni et est. Cum facilis consequuntur aliquid eligendi et. Nostrum molestiae modi neque nisi.
        Dolorem occaecati dolorem iure ut sint voluptate iste. Itaque magni possimus rerum.
        Repudiandae iste magnam id eos non. Veritatis consequuntur exercitationem est modi soluta.
        Et porro enim adipisci et est. Porro nulla ex rerum et dignissimos occaecati minus.
        Dolores eum et odio labore sapiente qui beatae. Sunt ea quisquam est enim delectus consectetur esse velit.
        Et quibusdam quos ipsam aperiam illum officiis.
        Recusandae odit magnam aut in officia. Veritatis optio qui harum ex nulla. Ullam quos perferendis possimus totam atque.
        Corporis ab est tempore nisi. Aut vero fugiat quae voluptas nemo. Eum aliquid error et quo omnis fugiat incidunt.
        Libero qui odit et. Aut iure sint quidem aut. Nam atque placeat harum molestiae non. Laudantium et rem voluptatem.
        Facilis ea similique dolores accusantium perferendis odit. Assumenda soluta illo laborum. Illo eum blanditiis minima.
        In debitis ipsam nostrum qui.
        Iure ut dolor sed et modi. Blanditiis cumque et quod dolores quae aut quo. Veritatis cum ut aut.
        Rerum optio asperiores earum ducimus natus laborum consequuntur.
      `
  }),
  components: {
    SideTooltip
  }
};
</script>

<style>
.paper-document {
  position: relative;
  font-size: 1.5em;
  background: #fff;
  box-shadow: 0 -1px 15px rgba(0, 0, 0, 0.2);
  max-width: 210mm;
  width: 100%;
  min-height: 80%;
  margin: 4rem auto;
  padding: 3rem;
}

.document-text {
  text-align: justify;
}

.underlined {
  text-decoration: underline;
  position: relative;
}

.side-tooltip {
  transition: opacity 0.5s ease;
  opacity: 0;
}

span.underlined:hover .side-tooltip {
  opacity: 1;
  transition-duration: 0.3s;
}
</style>
