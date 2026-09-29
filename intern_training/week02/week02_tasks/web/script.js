const dict = {
  title: "Shopping List",
  items: [
    {
      id: 1,
      name: "Apples",
      category: "Produce",
      inStock: true,
    },
    {
      id: 2,
      name: "Whole Milk",
      category: "Dairy",
      inStock: true,
    },
    {
      id: 3,
      name: "Sourdough Bread",
      category: "Bakery",
      inStock: false,
    },
  ],
};

const container = document.querySelector(".list");
const header = document.createElement("head");
header.textContent = dict["title"];
container.appendChild(header);

dict["items"].forEach((item) => {
  console.log(item);
  const li = document.createElement("li");
  li.textContent = `id: ${item.id}
    name: ${item.name}
    category:${item.category},
    inStock: ${item.inStock}`;
  container.appendChild(li);
});
