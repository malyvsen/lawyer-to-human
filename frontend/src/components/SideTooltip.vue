<template>
  <div class="tooltip-wrapper">
    <div class="side-tooltip elevation-7">
      <!-- {{ content }}	 -->
      <strong>
        <v-icon>book</v-icon>Definition
      </strong>
      <p>Lorem ipsum dolor sit amet enim. Etiam ullamcorper. Suspendisse a pellentesque dui, non felis.</p>
    </div>
  </div>
</template>

<script>
  export default {};
</script>

<style>
  .tooltip-wrapper {
    position: absolute;
    top: -1rem;
    width: 100vw;
  }

  .side-tooltip {
    position: absolute;
    left: -4rem;
    max-width: 19%;
    transform: translateX(-100%);
    background: #fff;
    /* box-shadow: 0 3px 20px rgba(0, 0, 0, 0.2); */
    padding: 1rem;
    padding-left: 0;
    font-size: 1.2rem;
    line-height: 1.4rem;
    text-align: left;
  }

  .side-tooltip p {
    margin: 1rem 0rem 0 3rem;
  }

  .side-tooltip strong i {
    vertical-align: -6px;
    padding: 0 5px 0 12px;
    color: rgb(13, 121, 209)!important;
  }

  .side-tooltip::after {
    content: "";
    position: absolute;
    right: -9px;
    top: 1em;
    width: 0;
    height: 0;
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
    border-left: 10px solid #fff;
  }
</style>

