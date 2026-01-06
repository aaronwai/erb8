$(document).ready(function () {
  $("#deleteConfirmModal").on("show.bs.modal", function (event) {
    const button = $(event.relatedTarget);
    const contactId = button.data("id");
    const deleteUrl = button.data("url");
    $("#modal-contact-id").text(contactId);
    $("#confirmDeleteBtn").attr("href", deleteUrl);
  });
  $("#confirmDeleteBtn").click(function (event) {
    $("#deleteConfirmModal").modal("hide");
    setTimeout(() => {
      window.location.href = $("#confirmDeleteBtn").attr("href");
    }, 300);
  });
});
