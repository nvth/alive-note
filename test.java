/*     */   @GetMapping({"/download"})
/*     */   public ResponseEntity<byte[]> getImage(@RequestParam("id") String id){
/*     */      try {
/* 187 */        HttpHeader headers = new HttpHeader();

/* 189 */        headers.add("Cache-Control", "no-cache, no-store");
/* 190 */        headers.add("Content-Disposition", "attachment; filename=soapbx.pdf");
/*     */
/* 192 */        byte[] image = this.downloadService.getPDF(id.replace("../", ""));
