# Request image generation using the correct active model endpoint
        response = client.models.generate_images(
            model='imagen-3.0-generate-002',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1, output_mime_type='image/jpeg'
            ),
        )

        image_found = False
        for generated_image in response.generated_images:
          image_found = True
          image_bytes = generated_image.image.image_bytes
          image = Image.open(BytesIO(image_bytes))

          st.success("Generation complete!")
          st.image(
              image, caption="Y2K Construction Baddie", use_container_width=True
          )
