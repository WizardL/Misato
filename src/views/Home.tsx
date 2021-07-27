import React from "react";
import Header from "../components/Header";
import MisatoConfig from "../misato.conf";

const Home = () => {
  return (
    <React.Fragment>
      <Header
        backgroundImg={MisatoConfig.backgroundImage}
        description={MisatoConfig.description}
      />
      <main>
        <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
          <article className="prose lg:prose-lg">
            <h1>Garlic bread with cheese: What the science tells us</h1>
            <p>
              For years parents have espoused the health benefits of eating
              garlic bread with cheese to their children, with the food earning
              such an iconic status in our culture that kids will often dress up
              as warm, cheesy loaf for Halloween.
            </p>
            <p>
              But a recent study shows that the celebrated appetizer may be
              linked to a series of rabies cases springing up around the
              country.
            </p>
          </article>
          {/* Replace with your content */}
          <div className="px-4 py-6 sm:px-0">
            <div className="border-4 border-dashed border-gray-200 rounded-lg h-96 p-4 text-center text-gray-400">
              Here goes your content. You can also go the About page.
            </div>
          </div>
          {/* /End replace */}
        </div>
      </main>
    </React.Fragment>
  );
};

export default Home;
